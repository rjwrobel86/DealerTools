#Parses "CSSR Playbook Manifest" list to make custom audiences for Google Ads 
#Input: "Playbook Manifest.csv"
#Output: "manifest_audience_4google.csv"

import pandas as pd

df = pd.read_csv('Playbook Manifest.csv')
df = df[['First Name', 'Last Name', 'Zip Code', 'Home Phone', 'Business Phone', 'Email Address']]

def add_leading_one(dataframe, column_name):
    mask = dataframe[column_name].notna()
    dataframe.loc[mask, column_name] = '1' + dataframe.loc[mask, column_name].astype(str)

add_leading_one(df, 'Home Phone')
add_leading_one(df, 'Business Phone')

def convert_column_to_int(dataframe, column_name):
    dataframe[column_name] = pd.to_numeric(dataframe[column_name], errors='coerce').astype(pd.Int64Dtype())

convert_column_to_int(df, 'Home Phone')
convert_column_to_int(df, 'Business Phone')

df['Country'] = 'US'

df.to_csv('manifest_audience_4google.csv', index=False)