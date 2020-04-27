'''
This file filters out the desired data from one .csv file given a .txt file containing the indices to be filtered out.
Assume you inside a working directory
'''

import os, json
import numpy as np 
import pandas as pd 

TXT = "text.txt"

with open(TXT) as f:
    indices = f.readlines()
    indices = [line.strip() for line in indices]

path_to_labels_file = "detailed.csv"
labels_df = pd.read_csv(path_to_labels_file)
labels_df = labels_df[labels_df.colname.isin(indices)] #colname is unique ID column.
labels_df.to_csv(path_to_labels_file, index=False)
