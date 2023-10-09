import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

def sin(x, amp=1):
    return np.sin(amp * x)

domain = np.arange(0, 100, 0.25)

print(domain)

noise = [np.random.randn(1)[0] for i in range(len(domain))]
print(noise)

range0 = list(map(sin, domain))

fig1, ax1 = plt.subplots()

ax1.plot(domain, range0)
ax1.set_title("pure-sine")
ax1.set_xlabel("time")

range_sum =[x + y for x, y in zip(range0, noise)]

fig2, ax2 = plt.subplots()
ax2.plot(domain, range_sum)

sig_fft = fftpack.fft(range_sum, len(range_sum))
amplitude = np.abs(sig_fft)
power = amplitude**2
sample_freq = fftpack.fftfreq(len(range_sum), 0.25)

print(len(sample_freq))
print(len(power))

fig3, ax3 = plt.subplots()
ax3.plot(sample_freq, power)


plt.show()

