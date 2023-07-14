#takes both ftp files from dominion, merges for relevant deets, then outputs csv for fb catalog


import pandas as pd
import os
import xml.etree.ElementTree as etree


os.system('curl -u USERNAME:PASSWORD ftps://FTPURL/FILENAME.csv -o inventory1.csv')

os.system('curl -u USERNAME:PASSWORD ftps://FTPURL/FILENAME.xml -o inventory2.xml')


tree = etree.parse("inventory2.xml")
print(tree)
root = tree.getroot()
print(root)
columns = ["vehicle_id", "vin","description"]
datatframe = pd.DataFrame(columns = columns)

for node in root:
    print(node)

for node in root:
    veh_id = node.attrib.get("vehicle_id")
    vin = node.find("vin").text if node is not None else None
    description = node.find("description").text if node is not None else None
    datatframe = datatframe.append(pd.Series([veh_id, vin, description], index = columns), ignore_index = True)

df1 = pd.read_csv("inventory1.csv", index_col=False)
df2 = pd.read_csv("inventory2.xml", index_col=False)

df1['image_url'] = df2['Image URL']
df1['final_url'] = df2['Final URL']
df1['sale_price'] = df1['price']
df1['brand'] = df1['make']
df1['link'] = df1['url']
df1['condition'] = df1['state_of_vehicle']
df1['id'] = df1['vehicle_id']
df1['image_link'] = df1['image_url']
df1['availability'] = "in stock"

df1.to_csv('fbinventory.csv', index=False)
