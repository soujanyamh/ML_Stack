import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

# Read Data
data = pd.read_csv("/kaggle/input/house-rent-prediction-dataset/House_Rent_Dataset.csv")

# Check The null values
sns.heatmap(data.isnull(), cmap=sns.cubehelix_palette(as_cmap=True))
data.isnull().sum()
