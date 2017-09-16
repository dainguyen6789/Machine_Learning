# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
clear
print ("Hello Spider Dai Nguyen")
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd #lib to import and manage dataset

dataset=pd.read_csv('Data.csv')

X=dataset.iloc[:,:-1].values #select all column except the last column
Y=dataset.iloc[:,3].values
