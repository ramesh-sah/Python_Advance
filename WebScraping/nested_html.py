import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

carts = soup.find_all('div', class_='caption')

product_names = []
product_prices = []
product_desc = []

for cart in carts:
    name = cart.find('a', class_='title').text
    product_names.append(name)

    price = cart.find(
        'h4', class_='float-end price card-title pull-right').text
    product_prices.append(price)

    description = cart.find('p', class_='description').text
    product_desc.append(description)

df = pd.DataFrame({"Product Name": product_names,
                  "Product Price": product_prices, "Product Desciption": product_desc})
df.to_excel("nested_products.xlsx")
