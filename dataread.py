#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
#~~~~~ Trial input ~~~~~#
#filename = 'dataread/DJ.csv'
#sep = ','


def extract_data(filename,sep):
    def extract_headers(R_data,sep):
        return R_data[0].split(sep)

    def extract_data_columns(R_data,ncols):
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


    f = open(filename,"r")
    raw_data = f.read().split('\n')
    headers = extract_headers(raw_data,sep)
    print(headers)
    columns = extract_data_columns(raw_data,len(headers))
    formatted_columns = []
    for col in enumerate(columns):
        #formatted_columns.append([])
        formatted_columns.append(np.array(col[1]))    

    Data = {}

    for h,c in zip(headers, formatted_columns):
        Data.update({h:c})

    return Data
