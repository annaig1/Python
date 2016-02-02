# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 13:37:55 2016

Un peu de traitement d'images

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
R

fig = plt.figure("mes images")
plt.clf()
ax=fig.add_subplot(2,2,1)
ax.set_title("Red")
plt.imshow(R, cmap = cm.gray)
plt.grid()
plt.colorbar()
ax=fig.add_subplot(2,2,2)
ax.set_title("Green")
plt.imshow(G, cmap = cm.gray)
plt.grid()
plt.colorbar()
ax=fig.add_subplot(2,2,3)
ax.set_title("Blue")
plt.imshow(B, cmap = cm.gray)
plt.grid()
plt.colorbar()
plt.show()