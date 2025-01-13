import pandas as pd
from datetime import datetime

df = pd.read_csv(r'D:\etl_project\data\customer_data.csv', delimiter='|')

# # Convert date columns to datetime format
df['Open_Date'] = pd.to_datetime(df['Open_Date'], format='%Y%m%d')
df['Last_Consulted_Date'] = pd.to_datetime(df['Last_Consulted_Date'], format='%Y%m%d')
df['DOB'] = pd.to_datetime(df['DOB'], format='%d%m%Y')

# # Calculate Age (in years)
df['Age'] = df['DOB'].apply(lambda x: (datetime.now() - x).days // 365)

# # Calculate Days Since Last Consulted
df['Days_Since_Last_Consulted'] = (datetime.now() - df['Last_Consulted_Date']).dt.days

# # Show the updated DataFrame
# print(df)

# # Validate mandatory columns
mandatory_columns = ['Customer_Name', 'Customer_Id', 'Open_Date']
for column in mandatory_columns:
    if df[column].isnull().any():
        print(f"Validation failed: {column} has null values.")

# Validate date formats
try:
    df['Open_Date'] = pd.to_datetime(df['Open_Date'], format='%Y%m%d')
except Exception as e:
    print(f"Date format error: {e}")

# Check if Customer_ID is unique
if df['Customer_Id'].duplicated().any():
    print("Validation failed: Customer_ID should be unique.")

df['Is_Active'] = df['Days_Since_Last_Consulted'] > 30
# df.to_csv('D:\etl_project\output\validation.csv')
df. to_csv(r'D:\etl_project\output\validation_final.csv', index=False) 