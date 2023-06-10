import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('../input/diamond-prices/diamonds.csv')
df.info()

# Type conversion
df['date'] = pd.to_datetime(df['date'])

# Check missing values
df.isnull().sum()

# Univariate analysis

# A. Categorical variables

# 1. Shape value counts
df['shape'].value_counts(dropna=False)

# 2. Colors value counts
df['color'].value_counts(dropna=False)

# 3. Clarity
df['clarity'].value_counts(dropna=False)

# 4. Cut
df['cut'].value_counts(dropna=False)

# 5. Symmetry
df['symmetry'].value_counts(dropna=False)

# 6. Polish
df['polish'].value_counts(dropna=False)

# B. Continuous variables

# Descriptive stats of continuous variables
df.describe().transpose()

# 1. Size (box plot + histogram of the size)
fig, axs = plt.subplots(1, 2, figsize=(16, 6))
df[['size']].boxplot(ax=axs[0])
df[['size']].hist(bins=20, ax=axs[1])

# 2. Price (log scale)
fig = plt.figure(figsize=(14, 12))
df[['total_sales_price']].hist()
ax = plt.gca()
ax.set_yscale('log')
ax.set_xlabel('Price')
ax.set_ylabel('Count')
fig.suptitle('Distribution of the total sale price on the log scale')
plt.tight_layout()

# 3. Depth_percent, table_percent, meas_length, meas_width, meas_depth
fig, axs = plt.subplots(3, 2, figsize=(16, 10))
sns.histplot(df['depth_percent'], kde=True, stat="count", linewidth=0, bins=10, ax=axs[0, 0])
sns.histplot(df['table_percent'], kde=True, stat="count", linewidth=0, bins=10, ax=axs[0, 1])
sns.histplot(df['meas_length'], kde=True, stat="count", linewidth=0, bins=10, ax=axs[1, 0])
sns.histplot(df['meas_width'], kde=True, stat="count", linewidth=0, bins=10, ax=axs[1, 1])
sns.histplot(df['meas_depth'], kde=True, stat="count", linewidth=0, bins=10, ax=axs[2, 0])
axs[2, 1].axis('off')
fig.tight_layout()

# Bivariate / Multivariate Analysis

# Size vs Price by Color
sns.lmplot(x='size', y='total_sales_price', hue='color', data=df.sample(20000), order=2, height=6, aspect=1.6)

# Clarity vs Log(Price) per Size
fig = plt.figure(figsize=(10, 8))
df['log_price'] = np.log(df['total_sales_price'])
df['log_price_by_size'] = df['log_price'] / df['size']
sorted_index = df[['clarity', 'log_price_by_size']].groupby('clarity').median().sort_values(by='log_price_by_size', ascending=False).index
sns.boxplot(x='log_price_by_size', y='clarity', data=df, order=sorted_index)

# Color vs Log(Price) per Size
fig = plt.figure(figsize=(10, 8))
sorted_index = df[['color', 'log_price_by_size']].groupby('color').mean().sort_values(by='log_price_by_size', ascending=False).index
sns.barplot(x='log_price_by_size', y='color', data=df, order=sorted_index)

# Pair plot for numeric variables
numbers_df = df[df.select_dtypes(include=np.number).columns[1:]].sample(2000)
sns.pairplot(numbers_df, diag_kind='kde', kind='reg', plot_kws={'scatter_kws': {'s': 1}, 'line_kws': {'color': 'grey'}})

# Showing the correlation matrix between all the variables
plt.figure(figsize=(8, 6))
sns.heatmap(data=numbers_df.corr(), annot=True, fmt='.2f', linewidths=.5, cmap='BuPu')

# Dummy variables

# Feature matrix (aka. predictors)
X = pd.concat([
    df[['size', 'depth_percent', 'table_percent', 'meas_length', 'meas_width', 'meas_depth']],
    pd.get_dummies(df['shape'], drop_first=True, prefix='shape'),
    pd.get_dummies(df['color'], drop_first=True, prefix='color'),
    pd.get_dummies(df['clarity'], drop_first=True, prefix='clarity'),
    pd.get_dummies(df['cut'], drop_first=True, prefix='cut'),
    pd.get_dummies(df['symmetry'], drop_first=True, prefix='symmetry'),
    pd.get_dummies(df['polish'], drop_first=True, prefix='polish'),
    pd.get_dummies(df['culet_size'], drop_first=True, prefix='culet_size'),
    pd.get_dummies(df['culet_condition'], drop_first=True, prefix='culet_condition')
], axis=1)

# Target vector
y = df['total_sales_price']

# Drop non-important features
X = X.drop(columns=['cut_Ideal', 'culet_size_S', 'culet_size_VL', 'cut_None', 'polish_Fair',
                    'culet_condition_Chipped', 'clarity_SI2', 'culet_size_M', 'cut_Fair'])

# Feature importance (OLS method)
import statsmodels.api as sm

ols_model = sm.OLS(y, X)
result = ols_model.fit()
print(result.summary2())
