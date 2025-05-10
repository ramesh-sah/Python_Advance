import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.find('div'))
price = soup.find_all('h4', {"class": "float-end price card-title pull-right"})
# print(price)
# for i in price:
#     print(i.string)
# print(price[3].string)

desc = soup.find_all('p', {"class": "description card-text"})
# print(desc)
print(desc[3].string)
for i in desc:
    print(i.string)
