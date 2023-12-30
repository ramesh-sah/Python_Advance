import requests
from bs4 import BeautifulSoup
for i in range(2, 12):
    url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=827155d3-a32d-42b6-bf37-a4149716d90c&page=" + \
        str(i)
    r = requests.get(url)
    print(r)
    print(url)

    soup = BeautifulSoup(r.text, "html.parser")
    np = soup.find("a", class_="_1LKTO3").get("href")
    cnp = "https://www.flipkart.com"+np
    print(r)
    print(cnp)
