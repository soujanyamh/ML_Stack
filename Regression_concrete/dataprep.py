# Removing outliers
def remove_outlier(df, col_name):
    plt.figure(figsize=(20, 20))
    f, axes = plt.subplots(1, 2, figsize=(12, 4))
    sns.boxplot(df[col_name], ax=axes[0], color='skyblue').set_title("Before Outlier Removal: " + col_name)
    Q1 = df[col_name].quantile(0.25)
    Q3 = df[col_name].quantile(0.75)
    IQR = Q3 - Q1
    df[col_name] = df[col_name].apply(
        lambda x: Q1 - 1.5 * IQR if x < (Q1 - 1.5 * IQR) else (Q3 + 1.5 * IQR if x > (Q3 + 1.5 * IQR) else x))
    sns.boxplot(df[col_name], ax=axes[1], color='pink').set_title("After Outlier Removal: " + col_name)
    print()
    plt.show()
    return df

for col in df.select_dtypes(exclude="object").columns[:-1]:
    df = remove_outlier(df, col)

# Defining the Target and Predictors Variables
X = df.drop("Strength", axis=1).values
y = df["Strength"]

# Splitting the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4, test_size=0.2)
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

# Normalizing the data
s = StandardScaler()
X_train = s.fit_transform(X_train)
X_test = s.transform(X_test)
