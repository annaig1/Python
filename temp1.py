# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.

Tracé d'une courbe 
@author: apedrant
"""
import numpy as np
import matplotlib.pyplot as plt

def mafonction(t, omega=1., tau=10.):
    """
    Une fonction mathématique
    
    Entrées :
    
    * t : temps
    * Omega : pulsation
    * tau : temps caractéristique
    
    Renvoie :
    Une sinusoide amortie.
    """
    return np.exp(-t/tau)*np.sin(omega*t)
    
x = np.array([1,2,3])
y=mafonction(x)

z=np.linspace(0.,10.,11)
w=mafonction(z)

t=np.linspace(0.,10.,1000)
omega=[1., 5., 10. ] #valeurs de omega


# Tracé de la figure 
plt.figure("Une figure")
plt.clf() # purge la figure
for o in omega:
    a=mafonction(t, omega=o)
    plt.plot(t, a, label="truc")
 # ou t,a, "or-", line... par exemple : marqueur rend et couleur rouge en pointillé
plt.legend()
plt.grid()
plt.xlabel("temps, $t$ [s] ")
plt.ylabel("Amplitude, $a$, [N]")
plt.show()