# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 15:25:16 2016

Un peu de fichiers 

@author: annaig
"""

import numpy as np

data = np.random.rand(100,4)

# Méthode 1 :
f=open("data.txt", "w")
for i in xrange(len(data)):
   for j in xrange(len(data[i])):
     f.write("{0:.2f}".format(data[i,j]))
   f.write("\n") 
f.close()  

# Méthode 2 :
np.savetxt("data_np.txt", data)   

# Charger un fichier
data2 = np.loadtxt("data.txt")

  
     
     
