import numpy as np
import matplotlib.pyplot as plt
pas = 20
tab_sum = []
tab = np.loadtxt("data.txt", dtype="int")
for i in range(int(len(tab)/pas)):
    tab_sum.append(np.sum(tab[i:i+pas]))
# print(len(tab_sum))

plt.plot(tab_sum)
plt.show()
