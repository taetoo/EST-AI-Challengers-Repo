import requests
from bs4 import BeautifulSoup

url = "https://novel.naver.com/webnovel/weekday"
res = requests.get(url)  # GET 메소드를 사용하여 url에 HTTP Request 전송
soup = BeautifulSoup(res.text, "html.parser")



webtoons = soup.find("div", attrs={"id": "integrationRaking"})
titles = webtoons.find_all("span", attrs={"class": "title"})

for title in titles:
    if title:
        print(title.get_text())
    else:

        print('No title found')  # 오류 시 메시지 출력