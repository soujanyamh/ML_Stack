### **Data Checks**
- Checking missing values
- Checking duplicates
- Checking data types of each column
- Checking the number of unique values of each column
- Checking statistics of data set
- Checking various categories present in different categorical column



# Checking missing values
df.isna().sum()

# Checking duplicates
df.duplicated().sum()

# Checking data types of each column
df.info()

# Checking the number of unique values of each column
df.nunique()

# Checking statistics of the dataset
df.describe()


# Function to remove outliers
def remove_outliers(df, column):
    percentile25 = df[column].quantile(0.25)
    percentile75 = df[column].quantile(0.75)
    iqr = percentile75 - percentile25
    upper_limit = percentile75 + 1.5 * iqr
    lower_limit = percentile25 - 1.5 * iqr
    df = df[(df[column] < upper_limit) & (df[column] > lower_limit)]
    return df

# Removing outliers
df = remove_outliers(df, 'Price')
df = remove_outliers(df, 'Number of Ratings')
df = remove_outliers(df, 'Number of Reviews')

# 3.2 Pie Charts

# 3.3 Multivariate Analysis
# Code for multivariate analysis goes here...

# 4. Transformation Pipeline
# Custom transformer for log scaling
class LogScaling(BaseEstimator, TransformerMixin):

    def fit(self, X):
        return self   

    def transform(self, X):
        return np.log1p(X)

class TransformationPipeline:

    def __init__(self) -> None:
        pass
    
    def preprocess(self):
        cat_cols = df.select_dtypes('object').columns
        num_cols = ['Number of Ratings', 'Number of Reviews']

        num_pipeline= Pipeline(
            steps=[
            ("imputer",SimpleImputer(strategy="median")),
            ("scaler",StandardScaler())
            ]
        ) 

        cat_pipeline=Pipeline(
            steps=[
            ("imputer",SimpleImputer(strategy="most_frequent")),
            ("one_hot_encoder",OneHotEncoder()),
            ("scaler",StandardScaler(with_mean=False))
            ]
        )

        preprocessor = ColumnTransformer([
            ("log_transform", LogScaling(), num_cols),
            ("num_pipeline", num_pipeline, num_cols),
            ("cat_pipelines",cat_pipeline,cat_cols)
            ], remainder= 'passthrough')
        
        return preprocessor
X = df.drop('Price', axis = 1)
y = df.Price



