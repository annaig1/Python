# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.

Tracé d'une courbe 
@author: apedrant
"""
import numpy as np

def mafonction(x):
    """
    Une fonction mathématique
    
    Entrées :
    
    * x : une variable
    
    Renvoie :
    Le carré de x
    """
    return x**2 # le carré de x
    
x = np.array([1,2,3])
y=mafonction(x)

z=np.linspace(0.,10.,11)
