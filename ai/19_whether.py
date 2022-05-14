from regex import P
import requests
import json
import time

key = ""
url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
params = {
    "serviceKey": key,
    "pageNo": "1",
    "numOfRows": "1000",
    "dataType": "JSON",
    "base_date": "20220513",
    "base_time": "0600",
    "nx": "58",
    "ny": "126",
}

response = requests.get(url, params=params)
time.sleep(1)
json_result = json.loads(response.content)
w_data = json_result["response"]["body"]["items"]["item"]

for temp in w_data:
    if temp["category"] == "PTY":
        if temp["obsrValue"] == "0":
            print("날씨맑음")
        elif temp["obsrValue"] == "1":
            print("비")
        elif temp["obsrValue"] == "2":
            print("비/눈")
        elif temp["obsrValue"] == "3":
            print("눈")
        elif temp["obsrValue"] == "4":
            print("소나기")
