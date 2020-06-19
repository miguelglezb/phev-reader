#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
#~~~~~ Trial input ~~~~~#
#filename = 'dataread/DJ.csv'
#sep = ','


def extract_data_columns(R_data,ncols,sep):
    Columns = []
    for i in range(ncols):
        Columns.append([])  
    for col in R_data[1:-1]:
        split_col = col.split(sep)
        for j in enumerate(Columns):
            try:
                j[1].append(float(split_col[j[0]]))
            except:
                j[1].append(split_col[j[0]])
    return Columns

def extract_data(filename,sep,pheaders=True):
    f = open(filename,"r")
    raw_data = f.read().split('\n')
    headers = raw_data[0].split(sep)

    if pheaders==True:
        print(headers) 

    columns = extract_data_columns(raw_data,len(headers),sep)
    formatted_columns = []
    for col in enumerate(columns):
        formatted_columns.append(np.array(col[1]))    

    Data = {}

    for h,c in zip(headers, formatted_columns):
        Data.update({h:c})
    return Data

def phantom_evdata(filename,pheaders=True):
    f = open(filename,"r")
    raw_data = f.read().split('\n')
    f.close()
    Row1 = raw_data[0]
    ncols = len(Row1.split(']'))-1
    l_side, r_side = Row1.find('[')+3, Row1.find(']')-1 
    width_header = Row1.find('[',Row1.find(']')) - Row1.find('[')
    headers, columns,  = [], []
    for i in range(ncols):
        headers.append(Row1[l_side+i*width_header:r_side+i*width_header].strip())
        columns.append([])
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
    return Data