import matplotlib.pyplot as plt
import numpy as np
from dephasage_traitement import *
from traitement_data import *
from math import pi, sin, cos

lst_fichier = ["data_440hz.txt"]

param_filtre = {}
param_filtre["fe"] = 400000  # Hz
param_filtre["fcb"] = 20000  # Hz
param_filtre["z"] = 1
param_filtre["fch"] = 200

d = 1*(10**(-2))
entree = [[[tps/(4*(10**5)) for tps in range(5000)], [sin(val/100 + k*cos(7*pi/10)*(10**(-2))/340*5000) for val in range(5000)]]
          for k in range(10)]
# entree = [filtrage(fichier, param_filtre) for fichier in lst_fichier]

for k in range(10):
    plt.plot(entree[k][0], entree[k][1])
plt.show()

pixels = 40
tab = []

for i in range(pixels):
    phi = i*(pi/pixels)
    somme = somme_signaux(entree, phi)
    tab.append(max(somme[1]))

tab = np.array(tab)
tab = np.expand_dims(tab, axis=0)

plt.imshow(tab, cmap='hot', interpolation='nearest')
plt.show()
