import re
import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.find('div'))
# price = soup.find('h4', {"class": "float-end price card-title pull-right"})
data = soup.find_all(['h4', 'a', 'p'])
# print(data)
# for i in data:
#     print(i.string)
# data = soup.find_all(string="Galaxy Tab 3")
# print(data)


# desc = soup.find('p', {"class": "description card-text"})

# desc = soup.find('p', class_="description")
# print(desc.string)

# using regex
data = soup.find_all(string=re.compile("Galaxy"))
print(data)
