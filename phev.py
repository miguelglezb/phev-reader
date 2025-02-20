#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import pandas as pd


##### For phantom .ev files, headers type ===>  [1 XX]  [2 YY]  [3 ZZ]   #####

def evreader(filename, pheaders=True, output='df'):
    f = open(filename,"r")
    raw_data = f.read().split('\n')
    f.close()
    Row1 = raw_data[0]
    ncols = len(Row1.split(']'))-1
    headers, columns,  = [], []
    for i in Row1.split("]")[:-1]:
        columns.append([])
        headers.append(i.strip('#').strip().strip("[").strip().lstrip('1234567890').strip())

    if pheaders==True:
        print(headers)

    for i in raw_data[1:]:
        if i.strip()=='':
            continue
        S = i
        for j in range(ncols):
            S = S.lstrip()
            if j < ncols-1:
                try:
                    columns[j].append(float(S[:S.find(' ')]))
                except:
                    columns[j].append(S[:S.find(' ')])
            else:
                try:
                    columns[j].append(float(S))
                except:
                    columns[j].append(S)
            S = S[S.find(' '):]

    formatted_columns = []
    for col in enumerate(columns):
        formatted_columns.append(np.array(col[1])) 

    Data = {}

    for h,c in zip(headers, formatted_columns):
        Data.update({h:c})
    if output=='df':
        return pd.DataFrame(Data)
    return Data




#Conversion of units from Phantom to cgs, day, year... 

class constants:
    mass = 1.989E33 
    time = 1.594E3 
    dist = 6.96E10
    vel = dist/time
    dens = mass/dist**3
    spangmom = dist**2/time
    spener = (dist/time)**2
    ener = mass*spener
    angmom = mass*spangmom
    pressure = ener/dist**3 
    yr = time/(24*3600*365)
    day = time/(24*3600)

    def __init__(self,mass=mass,time=time,dist=dist,yr=yr,day=day,
                    spangmom=spangmom,ener=ener,spener=spener,vel=vel,
                    angmom=angmom,dens=dens, pressure=pressure):
        """Phantom units in cgs"""
        self.G = G 
        self.mass = mass 
        self.time = time 
        self.dist = dist
        self.vel = vel
        self.dens = dens
        self.spangmom = spangmom
        self.spener = spener
        self.angmom = angmom
        self.ener = ener
        self.pressure = pressure
        self.yr = yr 
        self.day = day 
    
        
