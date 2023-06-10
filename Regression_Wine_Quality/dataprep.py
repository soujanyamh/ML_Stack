import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Read the dataset
data = pd.read_csv("/kaggle/input/wine-quality-data-set-red-white-wine/wine-quality-white-and-red.csv")

# Drop duplicates
data.drop_duplicates(inplace=True)

# Check for missing values
data.isnull().sum()

# Outlier treatment using IQR method
def outlier_treatment(column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)
    data[column] = np.where(data[column] < lower_bound, lower_bound, data[column])
    data[column] = np.where(data[column] > upper_bound, upper_bound, data[column])

# Apply outlier treatment to selected columns
columns_to_treat = ['fixedacidity', 'volatileacidity', 'citricacid', 'chlorides', 'freesulfurdioxide',
                    'totalsulfurdioxide', 'density', 'pH', 'sulphates', 'alcohol', 'residualsugar']
for column in columns_to_treat:
    outlier_treatment(column)

# Feature scaling using StandardScaler
scaler = StandardScaler()
data[columns_to_treat] = scaler.fit_transform(data[columns_to_treat])

# Convert quality column to categorical
data['quality'] = data['quality'].astype('category')

# Encode categorical variables
categorical_columns = ['type', 'quality']
for column in categorical_columns:
    data[column] = data[column].cat.codes

# Splitting the data into features and target variable
X = data.drop('quality', axis=1)
y = data['quality']
