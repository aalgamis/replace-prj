
import pandas as pd
import numpy as np

# return prom from Clearsky GHI per day

import datetime

path = "./datasets/NREL-radiation/nrel-radiation-2017.csv"

df = pd.read_csv(path, nrows=8761)

arr= np.zeros(366)

#print(arr)

for i in range(len(df)):
    day=int(df.iloc[i]["Day"])
    month=int(df.iloc[i]["Month"])
    day_of_year = int(datetime.date(2017, month, day).timetuple().tm_yday)#strftime("%Y%m%d%H%M%S"))
    arr[day_of_year] += df.iloc[i]["Clearsky GHI"]
    
    
print("values per day")
print(arr)

sumVals=0

for val in arr:
    sumVals+=val
    
prom = sumVals/len(arr)

print("prom value per year")
print(prom)
