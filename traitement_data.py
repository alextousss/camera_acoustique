import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


tab = np.loadtxt("data.txt", dtype="int")
l = len(tab)
nb_courbes = 6
courbes = np.zeros((nb_courbes, l))

print("Débutde l'acquisition des données")

for k in tqdm(range(1, nb_courbes)):
    pas = k*200
    courbes[k, 0] = sum(tab[0:pas])
    for i in range(1, len(tab) - pas):
        courbes[k, i] = courbes[k, i-1]-tab[i-1]+tab[i+pas]
    for i in range(0, len(tab) - pas):
        courbes[k, i] = courbes[k, i]/pas
    plt.plot(courbes[k, :-pas], label=str(pas))

print("Fin de l'acquisition des données")

# plt.legend()
# plt.show()

# Fréquence de coupure
fc = 500  # Hz
tau = 1/(2*np.pi*fc)

# Période d'échantillonnage
Te = 1/400000  # s

s_pb = np.zeros((nb_courbes, l))  # signal passe-bas
print("Début du filtrage")

for k in tqdm(range(1, nb_courbes)):
    for i in tqdm(range(1, len(courbes[k, :]))):
        s_pb[k, i] = (s_pb[k, i-1]+Te/tau*(courbes[k, i-1]-s_pb[k, i-1]))

    plt.plot(s_pb[k, pas:-pas], label=str(k*200))

print("Fin du filtrage")

plt.legend()
plt.show()

print("Début analyse FFT")

fft = np.zeros((nb_courbes, l))

"""
for k in tqdm(range(1, nb_courbes)):
    fft[k, :-2*pas] = np.fft.fft(s_pb[k, pas:-pas])
    freq = np.fft.fftfreq(len(s_pb[k, pas:-pas]), 1/Te)
    plt.plot(np.abs(fft[k, :]), label=str(k*200))
plt.legend()
plt.show()
"""
