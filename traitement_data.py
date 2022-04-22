import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


tab = np.loadtxt("data.txt", dtype="int")
l = len(tab)

# Fréquence de coupure
fc = 2000  # Hz
tau = 1/(2*np.pi*fc)

# Période d'échantillonnage
Te = 1/400000  # s

# filtre passe pas ordre 2
signal = [0, 0]
for i in range(1, l):
    signal.append(2*signal[i]-signal[i-1]+(Te/tau)**2*(tab[i]-signal[i]))
plt.plot(signal[500:])
plt.show()

print("Début analyse FFT")


fft = np.fft.fft(signal[500:])
freq = np.fft.fftfreq(len(signal[500:]), d=1/fc)
print(fft)
plt.plot(freq, np.abs(fft))
plt.legend()
plt.show()
