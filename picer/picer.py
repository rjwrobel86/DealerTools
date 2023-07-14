import os
import time
import requests
import pandas as pd

os.system("zsh dominion.sh")
time.sleep(3)

df = pd.read_csv("inventory.csv")

df = df[['ID', 'Image URL']] 
df.dropna(inplace=True)
urllist = df['Image URL'].to_list()
vinlist = df['ID'].to_list()

def download_images(vins, urls, output_directory):
    for vin, url in zip(vins, urls):
        response = requests.get(url)
        if response.status_code == 200:
            image_extension = os.path.splitext(url)[1]
            image_filename = f"{vin}{image_extension}"
            image_path = os.path.join(output_directory, image_filename)
            with open(image_path, "wb") as file:
                file.write(response.content)
            print(f"Downloaded and saved image {image_filename}")
        else:
            print(f"Failed to download image for identifier: {vin}")

output_directory = "vehicle_images"
os.makedirs(output_directory, exist_ok=True)

download_images(vinlist, urllist, output_directory)