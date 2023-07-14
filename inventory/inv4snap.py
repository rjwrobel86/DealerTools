#Snapchat Inventory
import os
import pandas as pd

os.system('zsh dominion.sh')

df = pd.read_csv('inventory.csv')

df = df[['ID','Item title','Sale price','Item description','Final URL','Image URL']]

columns={"Item title":"Title","Image URL":"Image Link","Sale price":"Price","Item description":"Description","Final URL":"Link"}
df = df.rename(columns=columns)

df['Availability'] = "In Stock"
df['Google Product Category'] = "916"

df.to_csv("urls4snap.csv")