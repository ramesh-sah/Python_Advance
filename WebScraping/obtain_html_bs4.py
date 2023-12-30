import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/"
r = requests.get(url)

# Pass the HTML content to BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")
# print(soup.div)
# print(soup.div.a)
# print(soup.div.p)
# print(soup.div.table)
# print(soup.header)
# print(soup.form)
# tag = soup.div.p
# print(tag.attrs)
# atb = (tag.attrs)
# print(atb["class"])
# print(tag.string)
tag = soup.header.div.a.button.span
print(tag.string)
