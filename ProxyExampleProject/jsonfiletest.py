import json
import requests

validproxy = []

# with open('f:\proxy.json', newline='') as jsonfile:
#     # data = json.loads(jsonfile)
#     # 或者這樣
#     data = json.loads(jsonfile.read())

# for item in data:
#     print(item)
#     r = requests.get('http://httpbin.org/ip',
#                      meta={'proxy': 'http://175.44.109.74:9999'})
#     print(r.status_code)
#     print(r.encoding)
#     break

url = 'https://httpbin.org/ip'
headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    # "Referer" : "http://www.xicidaili.com/nn/1"
}

proxies = {
    'http': 'http://167.172.238.236:3128',
    'https': 'https://205.141.197.38:8080'
}

r = requests.get("http://httpbin.org/ip", proxies=proxies, headers=headers)
print(r.text)
