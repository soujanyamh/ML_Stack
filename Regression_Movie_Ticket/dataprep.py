import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import sklearn.metrics as metrics

# Loading the dataset
data = pd.read_csv("/kaggle/input/cinema-ticket/cinemaTicket_Ref.csv")

# Dropping the null values
data.dropna(inplace=True)

# Checking for missing values again
print("The null values are dropped")
data.isnull().sum()

# Assigning X values based on correlation with y
X = data[['ticket_price', 'occu_perc', 'show_time', 'tickets_sold', 'ticket_use', 'capacity']]
Y = data['total_sales']

# Splitting the data into training and testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.7, random_state=42)

# Training the linear regression model
lr = LinearRegression()
lr.fit(X_train, Y_train)

# Predicting the data
y_pred = lr.predict(X_test)

# Plotting the predicted values against the actual values
plt.figure(figsize=(12, 6))
plt.scatter(Y_test, y_pred, color='b')
plt.show()

# Checking r2_score
r_squared = r2_score(Y_test, y_pred)
r_squared

# Checking other metrics
print('MAE: {}'.format(metrics.mean_absolute_error(Y_test, y_pred)))
print('MSE: {}'.format(metrics.mean_squared_error(Y_test, y_pred)))
print('RMSE: {}'.format(np.sqrt(metrics.mean_squared_error(Y_test, y_pred))))
