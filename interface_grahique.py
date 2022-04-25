import matplotlib.pyplot as plt
import numpy as np
from dephasage_traitement import *
from math import pi

entree = [[[0 for tps in range(5000)], [0 for val in range(5000)]]
          for k in range(10)]
tab = []

for i in range(20):
    phi = i*(pi/20)
    somme = somme_signaux(entree, phi)
    tab.append(max(somme[1]))


plt.imshow(tab, cmap='hot', interpolation='nearest')
plt.show()
