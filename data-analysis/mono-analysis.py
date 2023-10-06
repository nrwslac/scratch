import csv
import math
import numpy as np
from statistics import mean

def getdata(filename):
    with open(filename, newline='') as csvfile:
        posreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        posdiffsamples = []
        for row in posreader:
            posdiffsamples.append(float(row[0]))
    print(filename, end=" ")
    return posdiffsamples

def calcRMS(samples, scale):
    samples = list(map(lambda x: x**2, samples))
    total = sum(samples)
    rms = math.sqrt(total / len(samples))
    print(f'RMS is: {rms * scale} nrad')
def calcSTD(samples):
    numSamples = len(samples)
    avg = mean(samples) 
    samples = list(map(lambda x: (x - avg)**2, samples))
    total = sum(samples)
    stdDev = math.sqrt(total / numSamples)
    print(stdDev)
def calcFreqPlot(samples):
    numSamples = len(samples)
    return None



calcRMS(getdata('gpiposdiff.csv'), 1000)
calcSTD(getdata('gpiposdiff.csv'))

calcRMS(getdata('48unplugged.csv'), 1000)
calcRMS(getdata('gpi-unplugged.csv'), 1000)
calcRMS(getdata('bothunplugged.csv'), 1000)
calcRMS(getdata('mirrorunplugged.csv'), 1000)