# Dropping unnecessary ID column
df = df.drop('ID', axis=1)

# Converting categorical data to numerical

# Smoking status
df['Smoking status'] = df['Smoking status'].map({'Yes': 1, 'No': 0})

# Gender
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})

# Converting bedtime to Epoch
df['Bedtime'] = pd.to_datetime(df['Bedtime'], format='%Y-%m-%d %H:%M:%S')
df['Bedtime'] = df['Bedtime'].apply(lambda x: int(x.timestamp()))
df['Wakeup time'] = pd.to_datetime(df['Wakeup time'], format='%Y-%m-%d %H:%M:%S')
df['Wakeup time'] = df['Wakeup time'].apply(lambda x: int(x.timestamp()))

# Finding Null values
print(df.isnull().sum())

# Imputing null values
df['Awakenings'].fillna(df['Awakenings'].min(), inplace=True)
df['Caffeine consumption'].fillna(df['Caffeine consumption'].mean(), inplace=True)
df['Alcohol consumption'].fillna(df['Alcohol consumption'].mean(), inplace=True)
df['Exercise frequency'].fillna(df['Exercise frequency'].mean(), inplace=True)

# Checking duplicates
print(f'Duplicate count = {df.duplicated().sum()}')

# Removing outliers
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# Remove the outliers from the dataframe
df_1 = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

# Checking correlations
corrmat = df_1.corr()
plt.figure(figsize=(10, 10))
sns.heatmap(corrmat, annot=True, cmap='coolwarm')

# Dropping columns with low correlation
df_1 = df_1.drop(['Light sleep percentage'], axis=1)

# Dropping columns with low correlation with sleep efficiency
df_1 = df_1.drop(['Smoking status', 'Caffeine consumption', 'Age', 'Gender', 'Bedtime', 'Wakeup time', 'Sleep duration', 'Exercise frequency'], axis=1)

# Scaling Features
scaler = StandardScaler()
X = scaler.fit_transform(df_1.drop('Sleep efficiency', axis=1))
