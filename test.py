# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 13:41:47 2016

@author: annaig
"""

import struct

def lire_header(path):
    f = open(path)
    lines=f.readlines()
    f.close()
    out={}
    for line in lines:
        if "=" in line:
            key = line.split("=")[0].split()[0]
            if key in ["lines", "samples"]:
              out[key] = int(line.split("=")[1])
    
    return out
    
def read_data(path):
    f = open(path, "rb")
    out = np.fromfile(f, dtype=np.float32)
    f.close()
    return out
    
header_path = "BossonsDEM_ll8m.hdr"
header = lire_header(header_path)

data.path = "BossonsDEM_ll8m"
data = read_data(data_path)

