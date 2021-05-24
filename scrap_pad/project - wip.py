
import pandas as pd
import numpy as np

    
# Load Data



df_temperature = pd.read_csv('./temperature_nsw.csv')
df_temperature = df_temperature.drop('LOCATION', axis = 1)
df_temperature = df_temperature.drop_duplicates(subset = 'DATETIME', keep = 'first')

df_demand = pd.read_csv('./totaldemand_nsw.csv')
df_demand = df_demand.drop('REGIONID', axis = 1)
df_demand = df_demand.drop_duplicates(subset = 'DATETIME', keep = 'first')

result = pd.merge(df_temperature, df_demand, on="DATETIME")
#df_temperature # 220326
#df_demand # 196513

#result # 195947
#result = result.dropna()
#result # 195947 ==> There is no NA


result['year'] = pd.DatetimeIndex(result['DATETIME']).year
result['month'] = pd.DatetimeIndex(result['DATETIME']).month
result['day'] = pd.DatetimeIndex(result['DATETIME']).day


result['hour'] = pd.DatetimeIndex(result['DATETIME']).hour
result['minute'] = pd.DatetimeIndex(result['DATETIME']).minute
result['dayofweek'] = pd.DatetimeIndex(result['DATETIME']).dayofweek

result = result.drop('DATETIME', axis = 1)
print(result.head())
result.to_csv('input.csv', index = False)


# now workout the adjustment to align the temperture minutes.