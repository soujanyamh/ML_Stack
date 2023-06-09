### **Data Checks**
- Checking missing values
- Checking duplicates
- Checking data types of each column
- Checking the number of unique values of each column
- Checking statistics of data set
- Checking various categories present in different categorical column

df.isna().sum()

df.duplicated().sum()

df = df.drop_duplicates()

df.nunique()


