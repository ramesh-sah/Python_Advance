import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

names = soup.find_all('a', class_='title')
# print(names)
product_name = []
for i in names:
    name = i.text
    product_name.append(name)
# print(product_name)


prices = soup.find_all('h4', class_='float-end price card-title pull-right')
# print(prices)
product_prices = []
for i in prices:
    price = i.text
    product_prices.append(price)
# print(product_prices)

desc = soup.find_all('p', class_='description card-text')
# print(desc)
product_desc = []
for i in desc:
    des = i.text
    product_desc.append(des)
# print(product_desc)


reviews = soup.find_all('p', class_='float-end review-count')
product_reviews = []
for i in reviews:
    review = i.text
    product_reviews.append(review)
# print(product_reviews)

df = pd.DataFrame({"Name": product_name, "Price": product_prices,
                  " Description": product_desc, "Review ": product_reviews})
# df.to_csv("product_details.csv")
df.to_excel('product_details.xlsx')
