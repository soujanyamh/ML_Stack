#Removal of any Duplicate rows (if any)
df.drop_duplicates(inplace=True)

#Check for empty elements
nvc = pd.DataFrame(df.isnull().sum().sort_values(), columns=['Total Null Values'])
nvc['Percentage'] = round(nvc['Total Null Values'] / df.shape[0], 3) * 100

#Converting categorical Columns to Numeric
df3 = df.copy()
ecc = nvc[nvc['Percentage'] != 0].index.values
fcc = [i for i in cf if i not in ecc]

# One-Hot Binary Encoding
for i in fcc:
    if df3[i].nunique() == 2:
        df3[i] = pd.get_dummies(df3[i], drop_first=True, prefix=str(i))
    elif 2 < df3[i].nunique() < 17:
        df3 = pd.concat([df3.drop([i], axis=1), pd.get_dummies(df3[i], drop_first=True, prefix=str(i))], axis=1)

# Removal of outliers
df1 = df3.copy()
features1 = nf

for i in features1:
    Q1 = df1[i].quantile(0.25)
    Q3 = df1[i].quantile(0.75)
    IQR = Q3 - Q1
    df1 = df1[df1[i] <= (Q3 + (1.5 * IQR))]
    df1 = df1[df1[i] >= (Q1 - (1.5 * IQR))]
    df1 = df1.reset_index(drop=True)

df = df1.copy()
df.columns = [i.replace('-', '_') for i in df.columns]

# Standardization on Training set
std = StandardScaler()
Train_X_std = std.fit_transform(Train_X)
Train_X_std = pd.DataFrame(Train_X_std, columns=X.columns)

# Standardization on Testing set
Test_X_std = std.transform(Test_X)
Test_X_std = pd.DataFrame(Test_X_std, columns=X.columns)
