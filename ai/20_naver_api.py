# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import ssl
import json

# ssl._create_default_https_context = ssl._create_unverified_context

client_id = ""
client_secret = ""

encText = urllib.parse.quote("스타벅스")
count = 100

url = f"https://openapi.naver.com/v1/search/cafearticle?query={encText}&display={count}&start=1"  # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if rescode == 200:
    response_body = response.read()
    json_data = json.loads(response_body.decode("utf-8"))
    result_data = json_data["items"]

    des_list = []
    for temp in result_data:
        des_list.append(temp["description"])

    print(des_list)
else:
    print("Error Code:" + rescode)
