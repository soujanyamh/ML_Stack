import numpy as np
import pandas as pd
import os

# Data loading
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
df = pd.read_csv('/kaggle/input/fuel-consumption/Fuel_Consumption_2000-2022.csv')

# Data Processing
df.info()
df.isnull().sum()
df.describe().T
df['MAKE'].value_counts()
df['TRANSMISSION'].value_counts().plot.barh();

import seaborn as sns
sns.barplot(x='VEHICLE CLASS', y='FUEL CONSUMPTION', hue='YEAR', data=df);

x = df.drop(['MAKE', 'MODEL', 'VEHICLE CLASS', 'TRANSMISSION', 'FUEL', 'FUEL CONSUMPTION'], axis=1)
X_ = df[['MAKE', 'MODEL', 'VEHICLE CLASS', 'TRANSMISSION', 'FUEL']]
dms = pd.get_dummies(X_)
X = pd.concat([x, dms], axis=1)
Y = df['FUEL CONSUMPTION']

X
Y

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.35, random_state=42)
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)
