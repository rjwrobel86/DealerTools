#Input: "Playbook Manifest.csv"
#Output: Several CSVs
#Removes irrelevant columns and splits up "Playbook Manifest.csv" up by sales person

import pandas as pd
df = pd.read_csv("Playbook_Manifest.csv", skiprows = range(1, 9), index_col=False)

sm = ['LISTOFSALESPEOPLE']
cols = ['First Name', 'Last Name', 'City','State','Zip Code','Home Phone','Email Address', 'Year','Make','Model','Vehicle Delivery Date','In-Market Indicator','Onstar','Distance From Dealer','Sales Person']
df2 = df[cols]
d={}

df2 = df2[df2['In-Market Indicator'] == 'FAVOR GM']
df2 = df2[df2['Distance From Dealer'] < 50]
df2 = df2.dropna(subset=['In-Market Indicator'])
df2 = df2.dropna(subset=['Home Phone'])

#df2 = df2[df2['Zip Code'] == 'ZIPCODE']
#df2 = df2.loc[df2['Sales Person'] == 'SALESPERSONNAME']
#df2 = df2[df2['Sales Person'] == 'SALESPERSONNAME']

for i in sm:
    dfx = df2.loc[df2['Sales Person'] == i]
    dfx = df2[df2['Sales Person'] == i]
    d.update({i:dfx})
    d[i].to_csv(i + " Playbook.csv", index=False)