from ophyd import Component as Cpt, Device, EpicsSignalRO
from ophyd.status import UnknownStatusFailure
from pcdsdevices.epics_motor import BeckhoffAxis
import time
import sys

class AvgCalc():
    def __init__(self, name):
        self.filename = name
        self.read()
    def read(self):
        with open(self.filename) as f:
            self.lines = f.readlines()
            print(self.lines)
    def calcAvg(self, numDataPoints):
        i = 0
        print("calc avgs")
        while i < len(self.lines):
            if self.lines[i][0] == 'm' or self.lines[i][0] == 'M':
                current_axis = self.lines[i]
                i += 1
                avg = 0.0
                high = 0.0
                for j in range(numDataPoints * 2):
                    line = self.lines[i].strip().split()
                    if j == numDataPoints:
                        print(current_axis, avg / numDataPoints)
                        high = avg / numDataPoints
                        avg = 0
                    avg += float(line[0])
                    i += 1
                print(f"stroke:{high - avg / numDataPoints}")
                print(current_axis, avg / numDataPoints)
            else:
                i += 1


class AxisLimits(Device):
    axis = Cpt(BeckhoffAxis, '')
    axisEncoder = Cpt(EpicsSignalRO, ':PLC:nEncoderCount_RBV')

    def move(self, pos, record=False):
        try:
            status = self.axis.umv(pos)
            time.sleep(3)
            print(self.axis.position)
            if record == True:
                self.myLog(str(self.axis.position) + " ")
                self.myLog(str(self.axisEncoder.get()) + "\n")
        except UnknownStatusFailure:
            #axis throws this sometimes when hitting a limit switch
            #but so far proceeds safely
            if record == True:
                self.myLog(str(self.axis.position) + " ")
                self.myLog(str(self.axisEncoder.get()) + "\n")
            time.sleep(3)

    def hitLimit(self, high, low, n, limitDir):
        stroke = high - low
        self.verifyOp(high, low, n, limitDir, stroke)

        for i in range(n):
            if limitDir == "High":
                self.move(high, True)
                #backoff
                self.move(high - stroke * .10)
            elif limitDir == "Low":
                self.move(low, True)
                #backoff
                self.move(low + stroke * .10)

    def myLog(self, data):
        f = open("sample.txt", "a")
        f.write(data)
        f.close()

    def verifyOp(self, high, low, n, limitDir, stroke):
        units = self.axis.egu
        print(f"Axis Current position: {self.axis.position} {units}\n")
        print(f"Axis Current velocity: {self.axis.velocity.get()} {units}/s\n")
        if limitDir == "High":
            print(f"The Axis will move from {self.axis.position} {units} to {high} {units}\n")
            print(f"back to: {high - stroke * .10} {units}\n")
            print(f"and then to: {high} {units}\n")
            print(f"this will happen {n} times\n")
        elif limitDir == "Low":
            print(f"The Axis will move from {self.axis.position} {units} to {low} {units}\n")
            print(f"back to: {low + stroke * .10} {units}\n")
            print(f"and then to: {low} {units}\n")
            print(f"this will happen {n} times\n")

       
        verification = input("proceed? y/n")

        if verification == 'y':
            print("proceeding with plan")
        else:
            sys.exit("plan not authorized")











