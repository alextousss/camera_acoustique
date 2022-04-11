from math import sin, sqrt




def dephasage_signal_num(tab, delta_t):
    tps=tab[0]
    valeurs=tab[1]
    c=1
    t=0
    while t<delta_t:
        t+=tps[c]-tps[c-1]
        c+=1
    return ([tps[:len(tps)-1-c],valeurs[c:]]) ##avance la phase du signal


def traitement(s1, s2, phi) ##phi=angle d'ou provient le signal qu'on souhaite récupérer
    dist=sqrt(d^2-d*sin(phi))##dist=distance à déphaser en mètres entre s1 et s2
    delta_t=(dist/340)
    return (dephasage_signal_num(s1, delta_t),s2)


def somme_signaux(s1,s2):
    valeurs1=s1[1]
    valeurs2=s2[1]
    a=len(valeurs1)
    som=[[0 for k in range (a)] [0 for k in range (a)]]
    assert valeurs1=valeurs2
    for k in range (len(valeurs1)):