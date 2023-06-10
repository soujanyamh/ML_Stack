import pandas as pd
import re
from matplotlib import pyplot as plt

# Read the dataset
df_car_models = pd.read_csv("/kaggle/input/2023-car-model-dataset-all-data-you-need/Car_Models.csv")

# Drop rows with missing values
df_car_models = df_car_models.dropna()

# Clean the 'Price' column
df_car_models['Price'] = df_car_models['Price'].str.replace(',', '')
df_car_models['Price'] = df_car_models['Price'].str.replace('$', '')
cleaned_prices = [price.replace('Starting at ', '') for price in df_car_models["Price"]]

def convert_to_usd(value):
    value = str(value).replace(' ', '')
    
    if '£' in value:
        value = float(value.replace('£', '')) / 1.05
    
    elif '€' in value:
        value = float(value.replace('€', '')) / 1.2     
        
    elif ('Rs.' in value) or ('₹' in value):
        if 'Lakh' in value or 'lakhs' in value:
            if "-" in value:
                min_val, max_val = value.split('-')
                min_val = str(min_val).replace('lakhs','').replace('Lakh','')
                value = float(min_val.replace('Rs.', '').replace('₹','')) * 100000 / 74.5
                
            else:
                min_val = min_val.replace('lakhs','').replace('Lakh','')
                value = float(value.replace('Rs.', '').replace('₹','')) * 100000 / 74.5
        else:
            value = float(value.replace('Rs.', '')) * 74.5  

    elif ('Lakh' in value) or ('lakhs' in value):
        value = float(value.replace('lakhs', '').replace('Lakh','')) * 100000
        
    elif 'million' in value:
        value = float(value.replace('million', '')) * 1000000

    elif 'Billion' in value:
        value = float(value.replace('Billion', '')) * 1000000000
        
    elif "-" in value:
        min_val, max_val = value.split('-')
        value = float(min_val)

    return float(value)

converted_prices = [convert_to_usd(price) for price in cleaned_prices]
df_car_models['cleaned_prices'] = converted_prices

# Clean the 'Horsepower' column
df_car_models['Horsepower'] = df_car_models['Horsepower'].str.replace(',', '')
df_car_models['Horsepower'] = df_car_models['Horsepower'].str.extract(r'(\d+)', expand=False).astype(int)
