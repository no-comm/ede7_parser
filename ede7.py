import requests
from bs4 import BeautifulSoup as bs
import config
def collect():
    r = requests.get("https://ede7.ru/", headers=config.headers, cookies=config.cookies)
    soup = bs(r.text, "lxml")
    names = soup.find_all("a", class_="menu-submenu-section-header-wrapper intec-cl-text-hover")
    urls = []
    price = []
    name = []
    for i in names:
        urls.append("https://ede7.ru"+i['href'])
    for i in urls:
        r = requests.get(i)
        soup = bs(r.text, "html.parser")
        try:
            prices = soup.find("div", class_="catalog-element-banner-purchase-price")
            namel = soup.find("h1", class_="catalog-element-banner-header")
            name.append(namel.text)
            price.append(prices.text)
        except:
            prices = soup.find("div", class_="catalog-element-banner-purchase-price-old")
            namel = soup.find("h1", class_="catalog-element-banner-header")
            name.append(namel.text)
            price.append(prices)
    list = []
    list.append(price)
    list.append(name)
    return list