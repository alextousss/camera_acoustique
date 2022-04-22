import matplotlib.pyplot as plt


def cartographie(tab):
    plt.imshow(tab, cmap='hot', interpolation='nearest')
    plt.show()
