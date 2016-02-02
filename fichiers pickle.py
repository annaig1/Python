# -*- coding: utf-8 -*-
"""
Created on Mon Feb 01 15:51:21 2016

@author: annaig
"""

import numpy as np
import pickle

data=["truc", "machin", [1,2,3]]
    
f = open("data.pckl", "w")
pickle.dump(data, f)
f.close()

del data # on efface fonc

f=open("data.pckl", "r")
data2=pickle.load(f)
f.close()

