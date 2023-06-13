import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Importing Data
df = pd.read_csv('/kaggle/input/wind-speed-prediction-dataset/wind_dataset.csv')
df.head()
df.info()

# Cleaning Up Data
# We need to convert the DATE dtype from object to a datetime
df['DATE'] = pd.to_datetime(df['DATE'])
df['YEAR'] = df['DATE'].dt.year
df['MONTH'] = df['DATE'].dt.month
df['DAY'] = df['DATE'].dt.day
df.head()

# Removing the original date column
df = df.drop(['DATE'], axis=1)
df.info()

# Check for null values
df.isnull().sum().sum()
sns.heatmap(df.isnull())
df.isna().sum()

# Filling these values with 0
df.fillna(0, inplace=True)
df.isnull().sum().sum()

# Visualization
sns.heatmap(df.corr())
