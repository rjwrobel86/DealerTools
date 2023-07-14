#Input: VinSoluitons "SoldLogExport.csv"
#Output: Audience lists For Google Ads and Facebook Ads

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

fb_columns = {'First Name':'fn', 'Last Name':'ln', 'Country':'country', 'Email':'email', 'Phone':'phone', 'Zip':'zip'}
df_fb = df.rename(columns=fb_columns)
df_fb['country'] = 'us'
df_fb.to_csv('fb_audience.csv', index=False)