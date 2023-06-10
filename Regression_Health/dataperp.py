import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin

# Reading the Dataset
df = pd.read_csv('/kaggle/input/student-mental-health/Student Mental health.csv')

# Dropping rows with missing values
df = df.dropna(how='any', axis=0)

# Renaming column
df.rename(columns={'Choose your gender': 'gender'}, inplace=True)

# Data visualization code goes here (not part of data preprocessing)

# Data preprocessing code ends here
