import numpy as np
import matplotlib.pyplot as plt

pas = 1000
result = []
tab = np.loadtxt("data.txt", dtype="int")
for i in range(len(tab) - pas):
    result.append(0)
    for j in range(pas):
        result[i] += tab[i + j]
# print(len(tab_sum))

plt.plot(result)
plt.show()
