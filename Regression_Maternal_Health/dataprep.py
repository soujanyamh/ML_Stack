import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv("../input/maternal-health-risk-data/Maternal Health Risk Data Set.csv")

df['RiskLevel'].replace({"high risk": "3", "mid risk": "2", "low risk": "1"}, inplace=True)
df['RiskLevel'] = df['RiskLevel'].astype(float)