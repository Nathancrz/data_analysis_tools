#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 20:12:15 2024

@author: nathan
"""
def moyennage(t: list, X: list, T=1, align='center'):
    """
    Renvoie une version moyennée sur T secondes glissantes de la liste X et sa liste de temps adaptée
    IN : liste t de temps en secondes ordonée, liste X à lisser, T la période de moyennage
    OUT : tm et Xm les deux listes moyennées
    
    si align='center' les valeurs de tm sont décalées d'un demi intervalle
    si align='left' elles prennent la valeur de t au début de l'intervalle
    si align='right' elles prennent la valeur de t au début de l'intervalle
    """
    import numpy as np
    assert T <= t[-1]/2, 'On ne peut pas moyenner sur une période si longue !'
    tm, Xm = [], []
    dt = len(t)*T/t[-1]
    n = 0
    while (n+1)*T <= t[-1]:
        a, b = int(round(n*dt, 0)), int(round((n+1)*dt, 0))
        if align=='left':
            tm.append((n)*T)
        elif align=='right':
            tm.append((n+1)*T)
        else:
            tm.append((n+0.5)*T)
        Xm.append(np.mean(X[a:b]))
        n += 1
    return tm, Xm

#%% exemple
import numpy as np
import matplotlib.pyplot as plt

N = 369
t = np.linspace(0, 12, N)
X = 200*(np.random.random(N)-0.5)
tm1, Xm1 = moyennage(t, X, 0.1)
tm2, Xm2 = moyennage(t, X, 1)
plt.plot(t, X, alpha=0.5, label='données brutes')
plt.plot(tm1, Xm1, '--', label='T = 0.1s')
plt.plot(tm2, Xm2, 'o--', label='T = 1s')
plt.legend()
plt.xlabel('temps en s')
plt.ylabel('grandeur mesurée')
plt.title('Exemple de moyennage')