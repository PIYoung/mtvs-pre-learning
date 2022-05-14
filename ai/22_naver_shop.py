import urllib.request
import json


def naver_price(p_name):
    client_id = ""
    client_secret = ""
    encText = urllib.parse.quote(p_name)
    url = f"https://openapi.naver.com/v1/search/shop.json?query={encText}&sort=asc"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        json_data = json.loads(response_body.decode("utf-8"))

        result_data = {}
        result_data["브랜드명"] = json_data["items"][0]["brand"]
        result_data["제품명"] = json_data["items"][0]["title"]
        result_data["가격"] = json_data["items"][0]["lprice"]

        return result_data

