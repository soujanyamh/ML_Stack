import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

# Load the dataset
df = pd.read_csv('/path/to/dataset.csv')

# Drop unnecessary columns if needed
df = df.drop(columns=['column1', 'column2'])

# Check for missing values
df.isnull().sum()

# Plot histograms for each feature
plt.figure(figsize=(16, 14))
for i, column in enumerate(df.columns):
    plt.subplot(3, 3, i + 1)
    sns.histplot(df[column], bins=100, kde=True)
plt.show()

# Remove outliers
# Replace 'column_name' with the actual name of the column you want to filter outliers from
df = df[(df['column_name'] < upper_threshold) & (df['column_name'] > lower_threshold)]

# Normalize the features using MinMaxScaler
scaler = MinMaxScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

