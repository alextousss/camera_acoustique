import numpy as np
import matplotlib.pyplot as plt

fclock = 500000

tab = np.loadtxt("data_440hz.txt", dtype="int")
l = tab.shape[0]
temps = np.array([-tab[0, 1]]*l)
temps += tab[:, 1]
data = tab[:, 0]
#plt.plot(temps, tab[:, 0])
# plt.show()

result = []
pas = 700
temps_plot = temps[pas//2:-pas//2]
for i in range(pas//2, l - pas//2):
    result.append(0)
    for j in range(pas):
        result[i-pas//2] += data[i + j - pas//2]
    result[i-pas//2] = result[i-pas//2]/pas
moy = sum(result)/len(result)
for i in range(len(result)):
    result[i] = result[i]-moy
#plt.plot(temps_plot, result)
# plt.show()

# Fréquence de coupure
fc = 0.02  # Hz
tau = 1/(2*np.pi*fc)

# Période d'échantillonnage
Te = 1/50  # s

s_pb = []
s_pb.append(result[0])

# Filtrage
for i in range(1, len(result)):
    s_pb.append(s_pb[i-1]+Te/tau*(result[i-1]-s_pb[i-1]))

plt.plot(temps_plot, result, color='#0000cc', label='Signal')
plt.plot(temps_plot, s_pb, color='#cc0000', label='Signal filtré')
plt.legend()
plt.show()

fft = np.fft.fft(s_pb)
freq = np.fft.fftfreq(len(s_pb), 1/fclock)
plt.plot(freq, np.abs(fft), label="real")
#plt.plot(freq[0:50], fft.imag[0:50], label="imag")
plt.legend()


plt.show()
