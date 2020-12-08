#get 과 post 
# get : 작은 데이터 및 보안이 필요 없는 데이터 전송 시 사용 
# post : 큰 데이터 및 비밀번호처럼 보안이 필요한 데이터를 전송 시 사용

import requests
import re 
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

notebooks = soup.find_all("li", {"class": re.compile("^search-product")})
for notebook in notebooks:
    name = notebook.find("div", {"class": "name"}).get_text()
    price = notebook.find("strong", {"class": "price-value"}).get_text()
    print(name, price)
    