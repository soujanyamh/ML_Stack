import pandas as pd
import numpy as np

df = pd.read_csv('../input/electrity-prices/electricity_prices.csv')

# Converting columns to numeric
df['ForecastWindProduction'] = pd.to_numeric(df['ForecastWindProduction'], errors='coerce')
df['SystemLoadEA'] = pd.to_numeric(df['SystemLoadEA'], errors='coerce')
df['SMPEA'] = pd.to_numeric(df['SMPEA'], errors='coerce')
df['ORKTemperature'] = pd.to_numeric(df['ORKTemperature'], errors='coerce')
df['ORKWindspeed'] = pd.to_numeric(df['ORKWindspeed'], errors='coerce')
df['CO2Intensity'] = pd.to_numeric(df['CO2Intensity'], errors='coerce')
df['ActualWindProduction'] = pd.to_numeric(df['ActualWindProduction'], errors='coerce')
df['SystemLoadEP2'] = pd.to_numeric(df['SystemLoadEP2'], errors='coerce')

# Handling missing values
df = df.dropna()

# Selecting features and target variable
X = df[['Day', 'Month', 'ForecastWindProduction', 'SystemLoadEA', 'SMPEA', 'ORKTemperature', 'ORKWindspeed',
        'CO2Intensity', 'ActualWindProduction', 'SystemLoadEP2']]
y = df['SMPEP2']
