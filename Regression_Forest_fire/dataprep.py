import pandas as pd
import numpy as np

# Read dataset
df = pd.read_csv(r"/kaggle/input/forest-fires-prediction/forest_fires.csv")

# Check dataset size
df.shape

# Check for duplicates
df.duplicated().sum()

# Remove duplicates
df = df.drop_duplicates()
df.duplicated().sum()

# Check for null values
df.isna().sum()

# Convert categorical columns to numeric
df["month"] = df["month"].replace({'mar': 3, 'oct': 10, 'aug': 8, 'sep': 9, 'apr': 4, 'jun': 6, 'jul': 7, 'feb': 2, 'jan': 1, 'dec': 12, 'may': 5, 'nov': 11})
df["day"] = df["day"].replace({'fri': 5, 'tue': 2, 'sat': 6, 'sun': 7, 'mon': 1, 'wed': 3, 'thu': 4})

# Split into independent and dependent variables
x = df.iloc[:, :-1]
y = df["area"]

# Train-test split
from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=43)

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

xtrain = pd.DataFrame(scaler.fit_transform(xtrain), columns=xtrain.columns)
xtest = pd.DataFrame(scaler.transform(xtest), columns=xtest.columns)
