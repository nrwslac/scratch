import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

def sin(x, amp=1):
    return np.sin(amp * x)
#number samples
sample_duration = 30

#sample / sec
sample_freq = 200.0
N = int(sample_duration * sample_freq)
x = np.linspace(0.0, sample_duration, int(sample_freq * sample_duration), endpoint=False)

noise = [np.random.randn(1)[0] for i in range(len(x))]

#pure sin
pure_sine = np.sin(20 * 2.0 * np.pi * x) + np.sin(60 * 2.0 * np.pi * x) + np.sin(95 * 2.0 * np.pi * x)

fig1, ax1 = plt.subplots()
ax1.plot(x, pure_sine)
ax1.set_title("pure-sine")
ax1.set_xlabel("time")


noisy_sin =[x + y for x, y in zip(pure_sine, noise)]

#sig_fft = fftpack.fft(range_sum, len(range_sum))
fig2, ax2 = plt.subplots()
ax2.plot(x, noisy_sin)

yf = fft.fft(noisy_sin)
xf = fft.fftfreq(int(sample_freq * sample_duration), 1.0 / sample_freq)[:N//2]

fig3, ax3 = plt.subplots()
ax3.plot(xf, 2.0/N * np.abs(yf[0:N//2]))

plt.show()

#amplitude = np.abs(sig_fft)
#power = amplitude**2
#sample_freq = fftpack.fftfreq(len(range_sum), 0.25)

#print(len(sample_freq))
#print(len(power))

#fig3, ax3 = plt.subplots()
#ax3.plot(sample_freq, power)


