import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler

# Read the CSV file
df = pd.read_csv('../input/synchronous-machine-dataset/SynchronousMachine.csv')
df.rename(columns={'I_y':'Load Current', 'PF':'Power Factor',
                   'e_PF':'Power Factor Error', 'd_if':'Excitation Current Change',
                   'I_f':'Excitation Current'}, inplace=True)

# Function to explore major elements in a Dataset
def describe(df):
    columns = df.columns.to_list()
    ncol = df.describe().columns.to_list()
    ccol = []
    for i in columns:
        if ncol.count(i) == 0:
            ccol.append(i)
        else:
            continue
    print('Name of all columns in the dataframe:')
    print(columns)
    print('')
    print('Number of columns in the dataframe:')
    print(len(columns))
    print('')
    print('Name of all numerical columns in the dataframe:')
    print(ncol)
    print('')
    print('Number of numerical columns in the dataframe:')
    print(len(ncol))
    print('')
    print('Name of all categorical columns in the dataframe:')
    print(ccol)
    print('')
    print('Number of categorical columns in the dataframe:')
    print(len(ccol))
    print('')
    print('------------------------------------------------------------------------------------------------')
    print('')
    print('Number of Null Values in Each Column:')
    print('')
    print(df.isnull().sum())
    print('')
    print('')
    print('Number of Unique Values in Each Column:')
    print('')
    print(df.nunique())
    print('')
    print('')
    print('Basic Statistics and Measures for Numerical Columns:')
    print('')
    print(df.describe().T)
    print('')
    print('')
    print('Other Relevant Metadata Regarding the Dataframe:')
    print('')
    print(df.info())
    print('')
    print('')

describe(df)

# Create 3 categories for better visualization
df['Load Current Range'] = 0
for i in range(0, len(df)):
    if df['Load Current'][i] > 5:
        df['Load Current Range'][i] = 'High'
    elif df['Load Current'][i] < 4:
        df['Load Current Range'][i] = 'Low'
    else:
        df['Load Current Range'][i] = 'Fair'

# Outlier analysis and visualization
def outliers(df_column):
    q75, q25 = np.percentile(df_column, [75, 25])
    iqr = q75 - q25
    print('q75:', q75)
    print('q25:', q25)
    print('Inter Quartile Range:', round(iqr, 2))
    print('Outliers lie before', q25 - 1.8 * iqr, 'and beyond', q75 + 1.8 * iqr)
    print('Number of Rows with Left Extreme Outliers:', len(df[df_column < q25 - 1.8 * iqr]))
    print('Number of Rows with Right Extreme Outliers:', len(df[df_column > q75 + 1.8 * iqr]))
    print('')
    sns.histplot(data=df, x=df_column, hue="Load Current Range", multiple="stack", palette=oe)

outliers(df['Load Current'])
outliers(df['Power Factor'])
outliers(df['Power Factor Error'])
outliers(df['Excitation Current Change'])

# Handling missing values using KNNImputer
imputer = KNNImputer(n_neighbors=5)
df_filled = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Handling missing values using IterativeImputer
imputer = IterativeImputer()
df_filled = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

# Calculating Variance Inflation Factor (VIF) to identify multicollinearity
def calculate_vif(df):
    df_numeric = df.select_dtypes(include=[np.number])
    vif = pd.DataFrame()
    vif["Variable"] = df_numeric.columns
    vif["VIF"] = [variance_inflation_factor(df_numeric.values, i) for i in range(df_numeric.shape[1])]
    return vif

vif = calculate_vif(df_filled)
print(vif)

# Standard Scaling of data
scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df_filled), columns=df_filled.columns)
