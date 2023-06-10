import pandas as pd

# Read the dataset
df = pd.read_csv('/kaggle/input/video-games-sales/video_games_sales.csv')

# Check for missing values
df.isnull().sum()

# Drop rows with missing values
df = df.dropna()

# Check the data types
df.dtypes

# Perform any additional preprocessing steps as needed
# ...

# Print the updated dataframe
print(df.head())
