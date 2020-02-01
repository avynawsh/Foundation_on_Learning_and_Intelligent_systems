import pandas as pd
import numpy as np

df=pd.read_csv(r'/home/atoms/Downloads/cs747-pa1/checking/outputData2.csv')
print(df['reg'].mean())