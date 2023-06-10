import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("../input/daily-gold-price-historical-data/gold.csv")

# 6.1. New Dataframe with only 'close' Column
close_df = df[['close']]

# 6.2. Converting New Dataframe to Array
dataset = close_df.values

# 6.3. The number of Rows to train the Model on
training_data_len = math.ceil(len(dataset) * 0.8)

# 6.4. Normalization
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

# 6.5. Creating Training dataset
train_data = scaled_data[0:training_data_len, :]

# 6.6. Convert x_train and y_train to array
x_train = []
y_train = []
for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])
x_train, y_train = np.array(x_train), np.array(y_train)

# 6.7. Reshaping the data
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
