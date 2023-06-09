#Dropping unnecessary ID column
df = df.drop('ID',axis=1)

#Converting categorical datas to numerical

#smoking status
df['Smoking status'] = df['Smoking status'].map({'Yes': 1, 'No': 0})

#Gender
df['Gender'] =df['Gender'].map({'Male':1,'Female':0})

#Converting bedtime to Epoch
df['Bedtime'] = pd.to_datetime(df['Bedtime'], format='%Y-%m-%d %H:%M:%S')
df['Bedtime'] = df['Bedtime'].apply(lambda x: int(x.timestamp()))
df['Wakeup time'] = pd.to_datetime(df['Wakeup time'], format='%Y-%m-%d %H:%M:%S')
df['Wakeup time'] = df['Wakeup time'].apply(lambda x: int(x.timestamp()))

#Finding Null
print(df.isnull().sum())

# Imputing null values

df['Awakenings'].fillna(df['Awakenings'].min(), inplace=True)
df['Caffeine consumption'].fillna(df['Caffeine consumption'].mean(), inplace=True)
df['Alcohol consumption'].fillna(df['Alcohol consumption'].mean(), inplace=True)
df['Exercise frequency'].fillna(df['Exercise frequency'].mean(), inplace=True)

#checking duplicates
print(f'Duplicate count = {df.duplicated().sum()}')

