import requests
from bs4 import BeautifulSoup

# user-agent
agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
header_data = {"User-Agent": agent}
res = requests.get(
    "https://comic.naver.com/index",
    headers=header_data,
)

html = BeautifulSoup(res.text, "html.parser")
ol = html.find("ol", id="realTimeRankFavorite")
lis = ol.find_all("li")

webtoon_list = []
for li in lis:
    webtoon_list.append(li.find("a").text)

print(webtoon_list)
