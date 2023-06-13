# Drop unwanted columns
df.drop(columns=df.columns[-2:], axis=1, inplace=True)

# Drop rows with missing values (-200 indicates missing values)
df = df[df != -200].dropna().reset_index()

# Move the target column to the last index
target_col = df.pop('T')
df.insert(len(df.columns), 'T', target_col)
df.drop(columns=['Date', 'index'], inplace=True)

# Encode the 'Time' column using LabelEncoder
label_encoder = LabelEncoder()
df['Time'] = label_encoder.fit_transform(df['Time'])

# Select numerical columns
numerical_columns = df.select_dtypes(include=['int', 'float']).columns

# Perform standard scaling on numerical columns
scaler = StandardScaler()
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
