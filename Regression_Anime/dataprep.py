import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None

df = pd.read_csv("../input/anime-dataset/anime.csv", engine='python')

C = df['rating'].mean()
m = df['votes'].quantile(0.85)

df2 = df.loc[df['votes'] >= m]

def weight_rating(x, m=m, C=C):
    v = x['votes']
    R = x['rating']
    
    return (v / (v + m) * R) + (m / (m + v) * C)

df2['score'] = df2.apply(weight_rating, axis=1)
