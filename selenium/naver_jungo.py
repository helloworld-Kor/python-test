import requests
import sys
import io
import pprint
import re
from datetime import datetime
import time

keyword = input("찾고싶은 물건을 말하시오::::::::::::::>")
ccnt = input("몇개의 물량을 보시겠습니까:::::::::::>")

keyword = re.sub(" ", "%20", keyword)  # &od=1
url = "https://apis.naver.com/cafe-web/cafe-search-api/v1.0/trade-search/all?query={}&page=1&size={}".format(
    keyword, ccnt)
req = requests.get(url)
_json = req.json()
lists = _json.get("result").get("tradeArticleList")  # [0].get("productSale"))
jungo = []
# print(lists)
# pprint.pprint(lists[0])
for li in lists:
    articleId = "https://cafe.naver.com/joonggonara/"
    articleId += str(li.get("articleId"))
    writeTime = li.get("writeTime") / 1000
    li = li.get("productSale")
    cost = li.get("cost")
    product = li.get("productName")
    stats = li.get("saleStatus")
    juso = ""
    s = datetime.fromtimestamp(writeTime)
    for region in li.get("regionList"):
        # cnt += 1
        juso = str(region['regionName1'])
        juso += " " + str(region['regionName2'])
        juso += " "+str(region['regionName3'])
    jungo.append(
        (str(s), cost, product, stats, juso, articleId))
index = 0
for jun in jungo:
    index += 1
    print("{}::::{}".format(index, jun))
