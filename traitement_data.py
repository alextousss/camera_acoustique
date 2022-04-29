import numpy as np
import matplotlib.pyplot as plt


fichier = "data_440hz.txt"

param_filtre = {}
param_filtre["fe"] = 400000  # Hz
param_filtre["fcb"] = 20000  # Hz
param_filtre["z"] = 1
param_filtre["fch"] = 200  # Hz


def filtrage(fichier, param_filtre):
    tableau = np.loadtxt(fichier, dtype="int")

    fe = param_filtre["fe"]
    fcb = param_filtre["fcb"]
    z = param_filtre["z"]
    fch = param_filtre["fch"]

    # Fréquence d'échantillonage
    Te = 1/fe
    # Paramètre du filtre
    taub = 1/(2*np.pi*fcb)
    tauh = 1/(2*np.pi*fch)

    if len(tableau.shape) > 1:
        data = tableau[:, 0]
        l = len(data)
        temps = tableau[:, 1]
        temps = [temps[i]-temps[0] for i in range(l)]
    else:
        data = tableau
        l = len(data)
        temps = [Te*i for i in range(l)]

    def filtre_ph1(data, tauh, Te):
        signal = [0]
        for i in range(l-1):
            signal.append(data[i+1]-data[i]+signal[i]*(1-Te/tauh))
        return signal

    def filtre_pb1(data, taub, Te):
        # filtre passe bas ordre 1
        signal = [0]
        for i in range(1, l):
            signal.append((signal[i-1]+Te/taub*(data[i-1]-signal[i-1])))
        return signal

    def filtre_pb2(data, taub, Te, z):
        # filtre passe bas ordre 2
        s = [0, 0]
        k = 1/(2*z*taub/Te+(taub/Te)**2)
        p = 2*z*taub/Te+2*(taub/Te)**2-1
        for i in range(1, l):
            s.append(k*(data[i]+s[i]*p-s[i-1]*(taub/Te)**2))
        return s

    #signalpb11 = filtre_pb1(data, tau, Te)
    #signalpb12 = filtre_pb1(signalpb11, tau, Te)
    signalpb2 = filtre_pb2(data, taub, Te, z)
    signalphpb2 = filtre_ph1(signalpb2, tauh, Te)
    signaldata = signalphpb2

    return [temps, signaldata]


'''
#plt.plot(signalpb11[500:], label='pb ordre 1')
plt.plot(signalphpb2[1000:], label="phpb2")
#plt.plot(signalpb2[500:], label="pb ordre 2")
plt.legend()
plt.show()
'''

#l_signal = [signalpb11, signalphpb2, signalpb2]
l_signal = filtrage(fichier, param_filtre)[1]
l_label = ["TF du signal après un p-bas ordre 2 et un p-haut"]
#l_label = ['pb ordre 1', "phpb2", "pb ordre 2"]

for i in range(len(l_signal)):
    signal = l_signal[i]
    fft = np.fft.fft(signal[500:])
    freq = np.fft.fftfreq(len(signal[500:]), d=1/param_filtre["fe"])
    # print(fft)
    nbval = len(freq)//20

    plt.plot(freq[:nbval], np.abs(fft)
             [:nbval], label=l_label[i])

    fftmax = max(fft[:nbval])
    index_fftmax = list(fft[:nbval]).index(fftmax)
    fmax = freq[index_fftmax]
    print('fmax='+str(fmax))
    # for i in range(1, 5):
    #    plt.vlines(index_fmax*i, 0, max(np.abs(fft)[:nbval]), label='f'+str(i)+'='+str(fmax*i),
    #               linestyles='dashed')

plt.title("FFT du fichier "+fichier)
plt.legend()
plt.show()
