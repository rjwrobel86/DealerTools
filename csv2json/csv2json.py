import csv
import json

csv_file = "inventory.csv"

with open(csv_file, 'r') as file:
    csv_data = csv.DictReader(file)
    json_data = json.dumps(list(csv_data), indent=4)

with open('inventory.json', 'w') as file:
    file.write(json_data)
