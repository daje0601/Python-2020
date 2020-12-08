import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.title.get_text()) # 텍스트를 출력 
# print(soup.a) # soup객체에서 처음 발견되는 a element(태그)를 반환 
# print(soup.a.attrs) # a element의 속성정보를 반환 
# print(soup.a["href"])  # a element의 속성 값을 출력 
# 지금까지 공부한 것은 html 중에서 정확한 위치를 알았을때 사용할 수 있는 것이다 
# 그러나, 우리가 스크래핑 할 것들은 어디에 있는지 정확한 위치를 알 수 없다 
# 그래서 사용하는 것이 find라는 속성이다 
# find는 찾고자 하는 태그를 입력하고 해도이되는 첫번째 엘리먼트를 찾을 수 있다 
# print(soup.find("a", attrs={"class": "Nbtn_upload"}))

# #네이버 웹툰 인기순 리스트 받아오기 
# lank_list = soup.find("ol", {"class": "asideBoxRank"}).get_text().strip()
# print(lank_list)

#네이터 웹툰 인기순에서 1등 받아오기 및 a태그만 가져오기 
# rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a)

# # 받아온 rank01 -> rank02 -> rank03로 넘어가는 방법 
# rank1 = soup.find("li", attrs={"class": "rank01"})
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank2.get_text())
# print(rank3.get_text())
# # 3에서 2로 넘어가기 
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.get_text())
# #부모태그로 이동하기 
# print(rank1.parent)


webtoon = soup.find("div", {"class":"list_area daily_all"}).get_text()
print(webtoon)
# 위와 같이 작성을 하면 이름과 이름 사이의 공백이 같이 나오네.. 줄이는 방법을 아직 몰라..
# 아래와 같이 작성을 하니 내가 원하는대로 제목만 딱딱 출력이 되는구만
cartoons = soup.find_all("a", {"class": "title"})
for cartoon in cartoons:
    print(cartoon.get_text())

