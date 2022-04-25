from math import sin, sqrt, pi

d = 1*(10**(-2))

## Attention pb au niveau du déphasage => list out of range ##


def deph_avant_signal_num(tab, delta_t):
    tps = tab[0]
    valeurs = tab[1]
    c = 0
    t = 0
    while t < delta_t:
        t += tps[c+1]-tps[c]
        c += 1
    return ([tps[:len(tps)-1-c], valeurs[c:]])  # avance la phase du signal


def deph_arrière_signal_num(tab, delta_t):
    tps = tab[0]
    valeurs = tab[1]
    c = 0
    t = 0
    while t < delta_t:
        t += tps[c+1]-tps[c]
        c += 1
    return ([tps[c:], valeurs[:len(tps)-1-c]])

# phi=angle d'ou provient le signal qu'on souhaite récupérer


def traitement(lst_s, phi):
    res = []
    # dist=distance à déphaser en mètres entre s1 et s2
    dist = sqrt(d**2-(d*sin(phi))**2)
    delta_t = dist/340
    print(phi, delta_t*100000)
    print(phi, delta_t*100000)
    # if phi >= pi/2:
    for i in range(len(lst_s)):
        res.append(deph_avant_signal_num(lst_s[i], i*delta_t))
    # else:
        # for i in range(len(lst_s)):
        #res.append(deph_arrière_signal_num(lst_s[i], i*delta_t))
    return(res)


def taille_min(lst_s):         # récupère la taille de la plus petite liste
    taille = []
    for e in lst_s:
        taille.append(len(e[1]))
    return min(taille)


def somme_signaux(lst_s, phi):
    deph = traitement(lst_s, phi)            # déphase le signal
    t = taille_min(deph)
    res = [deph[0][0][:t], deph[0][1][:t]]           # res = [[tps],[val]]
    for i in range(1, len(deph)):              # parcours des signaux déphasés
        # parcours les valeurs du signal pour les sommer
        for j in range(t):
            res[1][j] += deph[i][1][j]
    return res
