import pandas as pd

new = pd.read_csv('new.csv')
used = pd.read_csv('used.csv')

new = new[['Lead Source Group', 'Total Leads', 'Good Leads','Sold from Leads']]
new.columns = ['Lead Source', 'New Vehicle Leads', 'Good New Vehicle Leads', 'New Vehicles Sold']
used = used[['Lead Source Group', 'Total Leads', 'Good Leads','Sold from Leads']]
used.columns = ['Lead Source', 'Used Vehicle Leads', 'Good Used Vehicle Leads','Used Vehicles Sold']

df = pd.merge(new, used, on="Lead Source", how="outer")

df = df.fillna(0)

df['Total Leads'] = df['New Vehicle Leads'] + df['Used Vehicle Leads']
df['Total Good Leads'] = df['Good New Vehicle Leads'] + df['Good Used Vehicle Leads']
df['Total Vehicles Sold'] = df['New Vehicles Sold'] + df['Used Vehicles Sold']

website_leads = df[df['Lead Source'].str.startswith('Website -')].groupby('Lead Source').sum()
website_leads = pd.DataFrame(website_leads.sum()).T
website_leads['Lead Source'] = 'Website'

df = df.loc[~df['Lead Source'].str.startswith('Website -'), :]
df = pd.concat([df, website_leads]).reset_index(drop=True)

numeric_cols = [cname for cname in df.columns if pd.to_numeric(df[cname], errors='coerce').notna().all()]
df.loc['Total'] = df[numeric_cols].sum()
df.loc['Total', 'Lead Source'] = 'Total'

df.to_csv('EOM Report Final.csv', index=False)