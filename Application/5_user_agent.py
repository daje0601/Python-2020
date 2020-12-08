import requests
url = "https://nadocoding.tistory.com"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()

# print("응답코드:", res.status_code)

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)
