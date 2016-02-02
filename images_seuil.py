# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 14:51:57 2016

@author: annaig
"""

import numpy as np
import matplotlib.pyplot as plt
import PIL
from matplotlib import cm

path="koala2.jpg" # chemin relatif car au même endroit que le logiciel
im = PIL.Image.open(path)
R, G, B= im.split() 
R = np.array(R)
G = np.array(G)
B=np.array(B)

Z = R
Zs = Z > 150

fig=plt.figure("mes images")
plt.clf()
ax = fig.add_subplot(2,2,1)
plt.imshow(Z, cmap =cm.gray)
ax.set_title("Original")
ax = fig.add_subplot(2,2,2)
plt.imshow(Zs, cmap =cm.gray)
ax.set_title("Seuil")
ax = fig.add_subplot(2,2,3)
plt.hist(Z.flatten(), bins = 250)
plt.show()

# np.ones([]) #matrice avec forme particulière