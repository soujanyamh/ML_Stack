import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Read the dataset
df = pd.read_csv('/kaggle/input/bitcoin-and-stock-exchanges/Dataset.csv')
df = df.set_index('Date')
df.index = pd.to_datetime(df.index)

# Fill missing values with the previous day's value
df = df.fillna(method='ffill')

# Normalize the data using Min-Max scaling
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns, index=df.index)

# Split the data into training and testing sets
train_size = int(len(df_scaled) * 0.8)
train_data = df_scaled[:train_size]
test_data = df_scaled[train_size:]
