import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('/kaggle/input/advertising-sales-dataset/Advertising Budget and Sales.csv')

# Drop the 'Unnamed: 0' column
df.drop('Unnamed: 0', axis=1, inplace=True)

# Rename the columns
df.columns = ['TV', 'Radio', 'Newspaper', 'Sales']

# Split the data into training and testing sets
A = df[['TV', 'Radio', 'Newspaper']]
B = df['Sales']
trainx, testx, trainy, testy = train_test_split(A, B, test_size=0.3, random_state=0)
