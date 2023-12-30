import requests
import pandas as pd
from bs4 import BeautifulSoup
Name = []
Prices = []
Description = []
Rating = []
for i in range(1, 300):
    url = 'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_2_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_2_0_na_na_na&as-pos=2&as-type=HISTORY&suggestionId=mobiles&requestId=827155d3-a32d-42b6-bf37-a4149716d90c&page=' + \
        str(i)
    r = requests.get(url)
    print(r)
    soup = BeautifulSoup(r.text, 'lxml')
    box = soup.find('div', class_="_1YokD2 _3Mn1Gg")

    names = box.find_all('div', class_="_4rR01T")
    print(len(names))
    for i in names:
        name = i.text
        Name.append(name)

    prices = box.find_all('div', class_="_30jeq3 _1_WHN1")
    print(len(prices))
    for i in prices:
        price = i.text
        Prices.append(price)

    desc = box.find_all('div', class_="fMghEO")
    print(len(desc))
    for i in desc:
        des = i.text
        Description.append(des)

    rating = box.find_all('span', class_="_1lRcqv")
    print(len(rating))
    for i in rating:
        rate = i.text
        Rating.append(rate)


df = pd.DataFrame({"Names": Name, 'Prices': Prices,
                  'Description': Description, "Rating": Rating})
df.to_excel("project2_mobiles.xlsx")
