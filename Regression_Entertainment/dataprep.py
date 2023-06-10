import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/imdb-most-popular-films-and-series/imdb.csv')
df.drop(['Name', 'Votes'], axis=1, inplace=True)
df.drop(df[df.Rate=='No Rate'].index, inplace=True)
df.drop(df[(df.Certificate == 'Not Rated') | (df.Certificate == 'Unrated')].index, inplace=True)

cols_include_none = ['Duration', 'Certificate', 'Nudity', 'Violence', 'Profanity', 'Alcohol', 'Frightening']

for col in cols_include_none:
    df.drop(df[(df[col]=='None') | (df[col]=='No Rate')].index, inplace=True)
df['Rate'] = pd.to_numeric(df['Rate'], downcast='float')
df['Duration'] = pd.to_numeric(df['Duration'], downcast='unsigned')

df.loc[df.Episodes == '-', 'Episodes'] = 1
df['Episodes'] = pd.to_numeric(df['Episodes'], downcast='unsigned')
df.Genre = df.Genre.str.replace(' ', '')
genre_cols = df.Genre.str.get_dummies(sep=',')

df.drop('Genre', axis=1, inplace=True)

df = pd.concat([df, genre_cols], axis=1)
categorical_cols = ['Type','Certificate', 'Nudity', 'Violence', 'Profanity', 'Alcohol', 'Frightening']

df = pd.get_dummies(df, columns=categorical_cols)

X = df.drop(['Rate'], axis=1)
y = df['Rate'].values
