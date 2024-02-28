import csv
import math
import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from scipy import fft

def getdata(filename):
    with open(filename, newline='', encoding='utf-8-sig') as csvfile:
        posreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        posdiffsamples = []
        for row in posreader:
            posdiffsamples.append(float(row[0]))
            #print(row[0])
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
    ax.plot(xf[100:], 2.0/N * np.abs(yf[100:N//2]))
    plt.show()
    return None



#calcRMS(getdata('gpiposdiff.csv'), 1000)
#calcSTD(getdata('gpiposdiff.csv'))

#calcRMS(getdata('48unplugged.csv'), 1000)
#calcRMS(getdata('gpi-unplugged.csv'), 1000)
#calcRMS(getdata('bothunplugged.csv'), 1000)
#calcRMS(getdata('mirrorunplugged.csv'), 1000)
#calcRMS(getdata('gpi-base-encoder-counts.csv'), 1000/150.)
calcRMS(getdata('mpi-error-enc-19102023.csv'), 1000 * 0.004505)
calcRMS(getdata('gpi-error-enc-19102023.csv'), 1000 / 150)

calcRMS(getdata('mpi-48unplugged-19102023.csv'), 1000 * 0.004505)
calcRMS(getdata('gpi-48unplugged-19102023.csv'), 1000 / 150)

calcRMS(getdata('mpi-withgpi-unplugged-19102023.csv'), 1000 * 0.004505)
calcRMS(getdata('gpi-withgpi-unplugged-19102023.csv'), 1000 / 150)

calcRMS(getdata('mpi-withmpi-unplugged-19102023.csv'), 1000 * 0.004505)
calcRMS(getdata('gpi-withmpi-unplugged-19102023.csv'), 1000 / 150)

#calcFreqPlot("gpi-base-encoder-diff", getdata('gpi-base-encoder-counts.csv'), 100)
#calcFreqPlot("mirror-pitch-act-posdiff", getdata('mirror-pitch-act-posdiff.csv'), 500)
#calcFreqPlot("mpi-base-encoder-diff", getdata('mpi-rms-error-enc-00.csv'), 100)
#calcFreqPlot("gpi-base-encoder-diff", getdata('gpi-rms-error-enc-00.csv'), 100)
calcFreqPlot("mpi-base-encoder-diff", getdata('mpi-error-enc-19102023.csv'), 100)
calcFreqPlot("gpi-base-encoder-diff", getdata('gpi-error-enc-19102023.csv'), 100)

calcFreqPlot("mpi-48unplugged-encoder-diff", getdata('mpi-48unplugged-19102023.csv'), 100)
calcFreqPlot("gpi-48unplugged-encoder-diff", getdata('gpi-48unplugged-19102023.csv'), 100)

calcFreqPlot("mpi-withgpi-unplugged", getdata('mpi-withgpi-unplugged-19102023.csv'), 100)
calcFreqPlot("gpi-withgpi-unplugged", getdata('gpi-withgpi-unplugged-19102023.csv'), 100)

calcFreqPlot("mpi-withmpi-unplugged", getdata('mpi-withmpi-unplugged-19102023.csv'), 100)
calcFreqPlot("gpi-withmpi-unplugged", getdata('gpi-withmpi-unplugged-19102023.csv'), 100)
