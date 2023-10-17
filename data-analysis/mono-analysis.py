import csv
import math
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from scipy import fft

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

def calcFreqPlot(filename, samples, freq):
    N = len(samples)
    yf = fft.fft(samples)
    xf = fft.fftfreq(N, 1 / freq)[:N//2]
    fig, ax = plt.subplots()
    ax.set_title(filename)
    ax.plot(xf, 2.0 /N * np.abs(yf[0:N//2]))
    plt.show()
    return None



calcRMS(getdata('gpiposdiff.csv'), 1000)
calcSTD(getdata('gpiposdiff.csv'))

calcRMS(getdata('48unplugged.csv'), 1000)
calcRMS(getdata('gpi-unplugged.csv'), 1000)
calcRMS(getdata('bothunplugged.csv'), 1000)
calcRMS(getdata('mirrorunplugged.csv'), 1000)
calcRMS(getdata('gpi-base-encoder-counts.csv'), 1000/150.)
calcFreqPlot("gpi-base-encoder-diff", getdata('gpi-base-encoder-counts.csv'), 100)
calcFreqPlot("mirror-pitch-act-posdiff", getdata('mirror-pitch-act-posdiff.csv'), 500)
