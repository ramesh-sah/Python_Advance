import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.find('div'))
# price = soup.find('h4', {"class": "float-end price card-title pull-right"})
# print(price.string)
# desc = soup.find('p', {"class": "description card-text"})
# # print(desc)
# print(desc.string)
desc = soup.find('p', class_="description")
print(desc.string)
