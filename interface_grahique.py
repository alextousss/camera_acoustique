import matplotlib.pyplot as plt
import numpy as np
from dephasage_traitement import *
from math import pi

entree = [[[tps/(4*(10**5)) for tps in range(5000)], [val for val in range(5000)]]
          for k in range(10)]
tab = []

for i in range(20):
    phi = i*(pi/20)
    somme = somme_signaux(entree, phi)
    tab.append(max(somme[1]))

tab = np.array(tab)
tab = np.expand_dims(tab, axis=0)

plt.imshow(tab, cmap='hot', interpolation='nearest')
plt.show()
