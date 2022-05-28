import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import true

def readcsvfiles(files):
    global df=pd.read_csv(files,index_col=0,parse_dates=True)
    return df

readcsvfiles('/Users/alexanderlindell/Documents/Programmering /Python/TNM098/Project/VC files/data/MobileSensorReadings.csv')
print(df)