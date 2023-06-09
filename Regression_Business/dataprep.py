import pandas as pd

# Read the dataset
df = pd.read_csv('/kaggle/input/advertising-sales-dataset/Advertising Budget and Sales.csv')

# Drop the 'Unnamed: 0' column
df.drop('Unnamed: 0', axis=1, inplace=True)

# Rename the columns
df.columns = ['TV', 'Radio', 'Newspaper', 'Sales']

# Split the data into input features (A) and target variable (B)
A = df[['TV', 'Radio', 'Newspaper']]
B = df['Sales']

