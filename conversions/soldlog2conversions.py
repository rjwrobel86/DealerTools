#Creates 'offline conversions' files from VinSolutions CRM sales log for digital marketing sales attribution on Facebook Ads and Google Ads
#input(s): "SoldLogExport.csv"
#output(s): "offline_conversions_fb.csv" and "offline_conversions_g.csv"

from datetime import datetime
import numpy as np
import pandas as pd

df = pd.read_csv('SoldLogExport.csv')
df = df[['GlobalCustomerID','AutoLeadID','SoldDate','FirstName','LastName','City','State','PostalCode','DayPhone','EvePhone','CellPhone','Email','EmailAlt','DealNumber','FrontGross','BackGross','VehicleVIN']]

def convert_date_time(input_date_time):
    dt = datetime.strptime(input_date_time, '%m/%d/%Y %I:%M:%S %p')
    output_date_time = dt.strftime('%Y-%m-%dT%H:%M:%S')
    return output_date_time

df['SoldDate'] = df['SoldDate'].map(convert_date_time)

df['Country'] = 'US'
df['Event Name'] = 'Purchase'
df['Currency'] = 'USD'
df['Value'] = df['FrontGross'] + df['BackGross']
df.loc[df['Value'] <= 0, 'Value'] = 1
df.drop(['FrontGross', 'BackGross'], axis=1, inplace=True)

column_dict = {'GlobalCustomerID':'Extern ID',
               'AutoLeadID':'Lead ID',
               'FirstName':'First Name',
               'LastName':'Last Name',
               'PostalCode':'ZIP/Postal Code',
               'DayPhone':'Phone number 1',
               'EvePhone':'Phone number 2',
               'CellPhone':'Phone number 3',
               'EmailAlt':'Email 2',
               'SoldDate':'Event Time',
               'VehicleVIN':'Item Number',
               'DealNumber':'Deal Number',
               'FrontGross':'Front Gross',
               'BackGross':'Back Gross'}

df.rename(columns=column_dict, inplace=True)

phone_number_columns = ["Phone number 1", "Phone number 2", "Phone number 3"]
for column in phone_number_columns:
    df[column] = '+1' + df[column].astype(str)
    df[column] = df[column].str.slice(0, -2)
    df[column] = df[column].replace('+1n', np.NaN)
    
float_columns = ['ZIP/Postal Code','Deal Number']
for column in float_columns:
    df[column] = df[column].astype(str)
    df[column] = df[column].str.slice(0, -2)

#Removed for testing purposes
df = df.drop('Deal Number', axis=1)
#df = df.drop('Extern ID', axis=1)

#Impute missing value fields with mean value
mean_value = df['Value'].mean()
df['Value'] = df['Value'].fillna(mean_value)
df['Value'] = df['Value'].round(2)

df.to_csv('offline_conversions_fb.csv', index=False)

gframe = df[['First Name','Last Name','Email','Phone number 2','Country','ZIP/Postal Code']]
#Phone number 2 is has least NaN values -per df.isna().sum()
gframe.rename(columns={'Phone number 2':'Phone','ZIP/Postal Code':'ZIP'})
gframe.to_csv('offline_conversions_g.csv', index=False)