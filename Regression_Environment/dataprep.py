import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data = pd.read_csv('../input/dissolved-oxygen-prediction-in-river-water/train.csv')
data.drop('Id', axis=1, inplace=True)

# Handling missing values
null_columns = list(data.columns[data.isna().sum() > 100])
data.drop(null_columns, axis=1, inplace=True)

# Dropping rows with any remaining missing values
data.dropna(axis=0, inplace=True)

# Splitting into features and target variable
y = data['target']
X = data.drop('target', axis=1)

# Scaling features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Splitting into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)
