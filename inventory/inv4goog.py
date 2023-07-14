import os
import pandas as pd
import pysftp

#Calls shell script to download feed.csv
os.system('zsh dominion.sh')

df = pd.read_csv('inventory.csv')
df = df[['Final URL', 'Item title']]
columns = {'Final URL':'Page URL','Item title':'Custom label'}
df.rename(columns=columns)

#Output for Google Ads dynamic page feed
df.to_csv('urls4google.csv', index=False)

#STFP interface
#cnopts = pysftp.CnOpts()
#cnopts.hostkeys = None
#with pysftp.Connection('IPADDRESS', username='USERNAME', password='PASSWORD', private_key=".ppk", cnopts=cnopts) as sftp:
#        #sftp.put('urls4google.csv') #Uploads a file
#        #sftp.get('urls4google.csv') #Downloads a file