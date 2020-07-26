#importing packages

import pandas as pd
import numpy as np
import os
from fbprophet import Prophet
# from sklearn import 
currentDirectory = os.path.dirname(os.path.abspath(__file__))
DataDirectory = os.path.join(currentDirectory,'Data')

Data = {}
for file in os.listdir(DataDirectory):
    data = pd.read_csv(os.path.join(DataDirectory,file),parse_dates=['Datetime'])
    Filename = file.split('_')[0]
    Data[Filename] = data
    
    
    
Train = Data['Train'].copy()
Test = Data['Test'].copy()
    

















