import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=758037&weekday="
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

# #title 가져오기
# titles = soup.find_all("td", {"class": "title"})
# for title in titles:
#     print(title.get_text().strip())

# #평점 평균내기 
# total_rate = 0
# webtoons = soup.find_all("div", {"class": "rating_type"})
# for webtoon in webtoons:
#     rate = webtoon.find("strong").get_text()
#     total_rate = total_rate + float(rate)

# print(total_rate)
# print(total_rate / len(webtoons))


