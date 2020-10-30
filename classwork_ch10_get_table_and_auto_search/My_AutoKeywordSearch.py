# e24.1AutoKeywordSearch.py
# ab00b
import requests
from bs4 import BeautifulSoup
import re
import json


def getKeywordResult(keyword):
    url = "http://www.baidu.com/s?wd=" + keyword
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        return ""


def parserLinks(html):
    soup = BeautifulSoup(html, "html.parser")
    results = []
    for div in soup.find_all("div", {"data-tools": re.compile("title")}):
        try:
            data = div.attrs["data-tools"]  # 获得属性值
            data_dict = json.loads(data)  # 将属性值转换成字典
            results.append(
                {"title": data_dict["title"], "link": data_dict["url"]}
            ) 
        except:
            print("Error" + data)
    return results


def main():
    html = getKeywordResult("Python书")
    results = parserLinks(html)
    count = 1
    for result in results:
        print("[{:^3}]{}\n{}".format(count, result["title"], result["link"]))
        count += 1
    

main()
