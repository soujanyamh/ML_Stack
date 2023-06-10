import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

plt.rcParams['figure.figsize'] = (15,10)
plt.style.use('ggplot')

from statsmodels.tsa.stattools import grangercausalitytests
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error

weather = pd.read_csv("../input/weather-analysis/climate_data.csv")
weather.head()

# Check for Null Values
print(weather.isnull().any())

# Removing Columns
print(weather.loc[weather["Date"] != weather["Date1"]])

# Dropping the columns I had justified dropping
weatherClean = weather.drop(["Average gustspeed (mph)", "Average direction (°deg)", "Rainfall for month (in)", "Rainfall for year (in)",
                        "Maximum rain per minute", "Maximum humidity (%)", "Minimum humidity (%)", "Maximum pressure", 
                        "Minimum pressure", "Maximum windspeed (mph)", "Maximum gust speed (mph)", "Maximum heat index (°F)",
                        "Date1", "Month", "diff_pressure"], axis=1)
weatherClean.head()

# Fixing the Labels
currentLabels = list(weatherClean.columns)
newLabels = ["Temperature", "Humidity", "Dewpoint", "Pressure", "Windspeed", "MaxTemperature", "MinTemperature"]
numLabels = len(newLabels)

for i in range(0, numLabels):
    weatherClean = weatherClean.rename(columns={currentLabels[i + 1]: newLabels[i]})

weatherClean.head()
print(weatherClean.dtypes)

# Set the Dates to the Index
weatherClean["Date"] = pd.to_datetime(weatherClean["Date"])
weatherClean.set_index("Date", inplace=True)
weatherClean = weatherClean.asfreq("D")

weatherClean.head(12)
pd.set_option('display.max_rows', 400)
print(weatherClean.isnull().any())
print(weatherClean.loc[weatherClean["Temperature"].isnull()])

