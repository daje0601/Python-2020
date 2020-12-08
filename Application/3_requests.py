# 1. html 내용 
# 2. xpath 
# 3. 
import requests
res = requests.get("https://naver.com")
res.raise_for_status()
print("웹 스크래핑을 진행합니다.")
# print("응답코드:", res.status_code)
