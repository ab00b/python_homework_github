# request.py
# ab00b
import requests
r=requests.get("http://cn.bing.com")
print(r.status_code,"\n",type(r))
# print(r.text)
print(len(r.content))
print(len(r.text))