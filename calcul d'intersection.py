#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:57:41 2024

@author: nathan

calcul du pourcentage de superposition de deux hiqtogrammes
"""

def intersection_histo(x1: list, y1: list, x2: list, y2: list, sortie_multiple=False) -> float:
    """
    Tous les arguments sont des outputs de np.histogram donc len(x)=n+1 et len(y)=n
    Les deux histogrammes doivent etre comparables, ie x1 = x2
    """
    largeur = (max(x_plage_av)-min(x_plage_av))/(len(x_plage_av)-1)
    n = len(y_plage_av)
    Sav, Sar, Sinter = 0, 0, 0
    for i in range(n):
        Sav += largeur*y_plage_av[i]
        Sar += largeur*y_plage_ar[i]
        Sinter += largeur*min((y_plage_av[i], y_plage_ar[i]))
    intersect = 100*Sinter/((Sav+Sar)/2)
    if sortie_multiple:
        return Sav, Sar, Sinter, intersect
    else:
        return intersect
    

#%% Exemple
import numpy as np
import matplotlib.pyplot as plt

N = 10000
t = np.linspace(0, 10, N) #100hz 
av = [np.random.normal(0.30*130, 25) for i in range(N)]
ar = [np.random.normal(0.35*130, 45) for i in range(N)]
y_plage_av, x_plage_av = np.histogram(av, bins=np.linspace(0, 130, 131))
y_plage_ar, x_plage_ar = np.histogram(ar, bins=np.linspace(0, 130, 131))

Sav, Sar, Sinter, intersect = intersection_histo(x_plage_av, y_plage_av, x_plage_ar, y_plage_ar, True)
    
plt.bar(x_plage_av[:-1], y_plage_av, width=1, alpha=0.65, align='edge', label='Av ' + str(int(Sav)) + ' surface')
plt.bar(x_plage_ar[:-1], y_plage_ar, width=1, alpha=0.65, align='edge', label='Ar ' + str(int(Sar)) + ' surface')
plt.plot((0), (0), label='Intersection '+str(round(100*Sinter/np.mean((Sar, Sav)), 1))+' %')
plt.xlabel("Tranche de position de 1 mm")
plt.ylabel("Nombre de valeurs")
plt.legend(loc='upper right')
plt.xlim(0, 130)
plt.title("Histogramme des positions")

