import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.nepalstock.com.np/today-price'
r = requests.get(url)
print(r.status_code)
# soup = BeautifulSoup(r.text, 'html.parser')

# table = soup.find('div', class_='widget-content')
# print(table)

# headers = table.find_all('th')
# titles = []

# for i in headers:
#     title = i.text
#     titles.append(title)
# df = pd.DataFrame(columns=titles)


# rows = table.find_all('tr')
# for i in rows[1:]:
#     data = i.find_all('td')
#     row = [tr.text for tr in data]

#     l = len(df)
#     df.loc[l] = row


# print(df)
# df.to_excel("stock_data.xlsx")
