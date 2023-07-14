import pysftp
import pandas as pd
import os

os.system('zsh dominion.sh')

df = pd.read_csv('inventory.csv')

df = df[['Final URL', 'Item title']]
df['Custom label'] = df['Item title']
df['Page URL'] = df['Final URL']
df = df[['Page URL','Custom label']]

df.to_csv('dpf_urls.csv', index=0)

#Using FTP instead of CSV upload
#cnopts = pysftp.CnOpts()
#cnopts.hostkeys = None
#with pysftp.Connection('FTPIPADDRESS', username='USERNAME', password='PASSWORD', private_key=".ppk", cnopts=cnopts) as sftp:
#        sftp.put('dpf_urls.csv')
#        sftp.get('file.csv')

