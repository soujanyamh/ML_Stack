import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('../input/fish-market/Fish.csv')
df = data.copy()

# Change column names
df.rename(columns={'Length1': 'LengthVer', 'Length2': 'LengthDia', 'Length3': 'LengthCro'}, inplace=True)

# Investigate missing values
print('Is there any NaN value in the dataset:', df.isnull().values.any())

# Different species and their counts
sp = df['Species'].value_counts()
sp = pd.DataFrame(sp)
sp.T
sns.barplot(x=sp.index, y=sp['Species'])
plt.xlabel('Species')
plt.ylabel('Counts of Species')
plt.show()

# Correlation of the variables
df.corr()
sns.heatmap(df.corr(), annot=True, cmap='YlGnBu')
g = sns.pairplot(df, kind='scatter', hue='Species')

# Basic statistics of the dataset
df.describe().T

# Analysing and dealing with outliers
sns.boxplot(x=df['Weight'])

dfw = df['Weight']
dfw_Q1 = dfw.quantile(0.25)
dfw_Q3 = dfw.quantile(0.75)
dfw_IQR = dfw_Q3 - dfw_Q1
dfw_lowerend = dfw_Q1 - (1.5 * dfw_IQR)
dfw_upperend = dfw_Q3 + (1.5 * dfw_IQR)
dfw_outliers = dfw[(dfw < dfw_lowerend) | (dfw > dfw_upperend)]

sns.boxplot(x=df['LengthVer'])
dflv = df['LengthVer']
dflv_Q1 = dflv.quantile(0.25)
dflv_Q3 = dflv.quantile(0.75)
dflv_IQR = dflv_Q3 - dflv_Q1
dflv_lowerend = dflv_Q1 - (1.5 * dflv_IQR)
dflv_upperend = dflv_Q3 + (1.5 * dflv_IQR)
dflv_outliers = dflv[(dflv < dflv_lowerend) | (dflv > dflv_upperend)]

sns.boxplot(x=df['LengthDia'])
dfdia = df['LengthDia']
dfdia_Q1 = dfdia.quantile(0.25)
dfdia_Q3 = dfdia.quantile(0.75)
dfdia_IQR = dfdia_Q3 - dfdia_Q1
dfdia_lowerend = dfdia_Q1 - (1.5 * dfdia_IQR)
dfdia_upperend = dfdia_Q3 + (1.5 * dfdia_IQR)
dfdia_outliers = dfdia[(dfdia < dfdia_lowerend) | (dfdia > dfdia_upperend)]

sns.boxplot(x=df['LengthCro'])
dfcro = df['LengthCro']
dfcro_Q1 = dfcro.quantile(0.25)
dfcro_Q3 = dfcro.quantile(0.75)
dfcro_IQR = dfcro_Q3 - dfcro_Q1
dfcro_lowerend = dfcro_Q1 - (1.5 * dfcro_IQR)
dfcro_upperend = dfcro_Q3 + (1.5 * dfcro_IQR)
dfcro_outliers = dfcro[(dfcro < dfcro_lowerend) | (dfcro > dfcro_upperend)]

# Outliers removed dataset
df_no_outliers = df[~((df['Weight'] < dfw_lowerend) | (df['Weight'] > dfw_upperend) |
                     (df['LengthVer'] < dflv_lowerend) | (df['LengthVer'] > dflv_upperend) |
                     (df['LengthDia'] < dfdia_lowerend) | (df['LengthDia'] > dfdia_upperend) |
                     (df['LengthCro'] < dfcro_lowerend) | (df['LengthCro'] > dfcro_upperend))]

# Save the preprocessed data to a new CSV file
df_no_outliers.to_csv('fish_preprocessed.csv', index=False)
