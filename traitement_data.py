import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


tab = np.loadtxt("data.txt", dtype="int")
l = len(tab)
nb_courbes = 6
courbes = np.zeros((nb_courbes, l))

for k in tqdm(range(1, nb_courbes)):
    pas = k*200
    for i in range(len(tab) - pas):
        for j in range(pas):
            courbes[k, i] += tab[i + j]
        courbes[k, i] = courbes[k, i]/pas
    # print(len(tab_sum))

    plt.plot(courbes[k, :-pas], label=str(pas))

plt.legend()
plt.show()

# Fréquence de coupure
fc = 0.22  # Hz
tau = 1/(2*np.pi*fc)

# Période d'échantillonnage
Te = 1  # s

s_pb = np.zeros((nb_courbes, l))

# Filtrage
for i in range(1, len(result)):
    s_pb.append(s_pb[i-1]+Te/tau*(result[i-1]-s_pb[i-1]))

plt.plot(result, color='silver', label='Signal')
plt.plot(s_pb, color='#cc0000', label='Signal filtré')
plt.show()
