#Input: VinSoluitons "SoldLogExport.csv"
#Output: Audience list For Google Ads

import numpy as np
import pandas as pd

df = pd.read_csv('SoldLogExport.csv')

df = df[['FirstName', 'LastName', 'PostalCode', 'Email', 'EmailAlt', 'DayPhone', 'EvePhone', 'CellPhone']]

df['Country'] = 'USA'

def convert_column_to_int(dataframe, column_name):
    dataframe[column_name] = pd.to_numeric(dataframe[column_name], errors='coerce').astype(pd.Int64Dtype())

convert_column_to_int(df, 'EvePhone')
convert_column_to_int(df, 'DayPhone')
convert_column_to_int(df, 'CellPhone')
convert_column_to_int(df, 'PostalCode')

def add_leading_one(dataframe, column_name):
    mask = dataframe[column_name].notna()
    dataframe.loc[mask, column_name] = '1' + dataframe.loc[mask, column_name].astype(str)

add_leading_one(df, 'EvePhone')
add_leading_one(df, 'DayPhone')
add_leading_one(df, 'CellPhone')


columns = {'FirstName':'First Name','LastName':'Last Name','PostalCode':'Zip','DayPhone':'Phone','EvePhone':'Phone','CellPhone':'Phone','EmailAlt':'Email'}
df = df.rename(columns=columns)

df.to_csv('google_audience.csv', index=False)