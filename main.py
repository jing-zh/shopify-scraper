import requests
import json
import pandas as pd
url = '<website_url>'


r = requests.get(url)

data = r.json()

product_list = []

for item in data['products']:
    title = item['title']
    handle = item['handle']
    created = item['created_at']
    product_type = item['product_type']

    for image in item['images']:
        try:
            imagesrc = image['src']
        except:
            imagesrc = "None"
    
    for variant in item ['variants']:
        price = variant['price']
        material = variant['title']
        available = variant['available']
        

        product = {
            'title': title,
            'handle': handle,
            'created': created,
            'product_type': product_type,
            'image': imagesrc,
            'price': price,
            'mateiral': material,
            'available': available,
        }

        product_list.append(product)


df = pd.DataFrame(product_list)

df.to_csv('testrun.csv')

print('save to file.')