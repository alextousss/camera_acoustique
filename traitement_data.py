import numpy as np
import matplotlib.pyplot as plt

pas = 500
result = []
tab = np.loadtxt("data.txt", dtype="int")
for i in range(len(tab) - pas):
    result.append(0)
    for j in range(pas):
        result[i] += tab[i + j]
# print(len(tab_sum))

plt.plot(result)
plt.show()

# Fréquence de coupure
fc = 0.22  # Hz
tau = 1/(2*np.pi*fc)

# Période d'échantillonnage
Te = 1  # s

s_pb = []
s_pb.append(result[0])

# Filtrage
for i in range(1, len(result)):
    s_pb.append(s_pb[i-1]+Te/tau*(result[i-1]-s_pb[i-1]))

plt.plot(result, color='silver', label='Signal')
plt.plot(s_pb, color='#cc0000', label='Signal filtré')
plt.show()
