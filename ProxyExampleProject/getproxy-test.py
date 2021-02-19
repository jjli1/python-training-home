import requests
from bs4 import BeautifulSoup
import random
import concurrent.futures
import json

# get the list of free proxies


def getProxies():
    r = requests.get('https://free-proxy-list.net/')
    # r = requests.get('http://www.us-proxy.org')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('tbody')
    proxies = []
    for row in table:
        # if row.find_all('td')[4].text == 'elite proxy':
        proxy = (lambda schema: 'https://' if schema == 'yes' else 'http://')(row.find_all('td')[6].text)+':'.join([row.find_all('td')[0].text,
                                                                                                                    row.find_all('td')[1].text])
        proxies.append(proxy)
        # else:
        #     pass
    return proxies


def extract(proxy):
    # this was for when we took a list into the function, without conc futures.
    # proxy = random.choice(proxylist)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:
        # change the url to https://httpbin.org/ip that doesnt block anything
        r = requests.get('https://httpbin.org/ip', headers=headers,
                         proxies={'https': proxy, 'http': proxy}, timeout=3)
        print('-->', r.json(), r.status_code,
              '<--', json.loads(r.text)['origin'])

        return proxy
    except Exception as e:
        pass
    return None


fineProxies = []
proxylist = getProxies()

# print((proxylist))
# extract('http://96.96.123.154:80')

# # check them all with futures super quick
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(extract, proxylist)

for result in results:
    if result:
        fineProxies.append(result)
print(fineProxies)
