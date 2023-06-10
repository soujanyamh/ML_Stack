import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/openintro-possum/possum.csv')
df.head()

for i in df[['site','Pop','sex','age']]:
    exec(f"df_{i} = pd.DataFrame(df[i].value_counts())")

df[cat_var[0]] = df[cat_var[0]].map({'Vic':0, 'other':1})
df[cat_var[1]] = df[cat_var[1]].map({'m':1, 'f':0})

outlier_col = ['hdlngth','skullw']
df = df[df['hdlngth']<100]
df = df[df['skullw']<67]

Model_df = df[['Pop','sex','skullw',dv]]
