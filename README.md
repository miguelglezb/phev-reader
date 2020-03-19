# dataread
# Module to read datafiles

# Hi, my name is Miguel Gonzalez and I'm doing a python script that should (eventually) read any data in columns and extract the information in the easiest way. 

# This is the first version, which should read any file with this basic format:

Column_1  ***SEPARATOR*** COLUMN_2  ***Sepatator*** COLUMN_3  ***Separator*** ...   
Data_11                   Data_21                   Data_31
Data_12                   Data_22                   Data_32
Data_13                   Data_23                   Data_33
   .                         .                         .
   .                         .                         .
   .                         .                         .
   
# The script works like this:

import dataread as dr

Data=dr.extract_data(filename,sep)

Data['Column_1']=[Data_11,Data_12,Data_13,...]
Data['Column_2']=[Data_21,Data_22,Data_23,...]

# filename is the name of the file (duh), and this version can read .txt and .csv 
# sep is the separator (commas, tab, slash, etc)
# So far I haven't tried other extensions or formats, but I doubt it works on binary or if the separator is ambiguous (doble space or double tab on different columns)
# If the columns are floats, integer or scientific notation it should put them in a numpy array, so operators (sum, product, etc) should work on said columns
# Other kind of elements in the columns should be left as strings, including dates in the formats DD/MM/YYY, DD-MM-YYYY, MM/DD/YYY, MM-DD-YYYY, etc

