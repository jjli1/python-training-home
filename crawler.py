import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
})
# with req.urlopen(url) as response:
#     data=response.read().decode("utf-8")
# print(data)
with req.urlopen(request) as response:
     data=response.read().decode("utf-8")

# print(data)

import bs4
# pip install lxml
root=bs4.BeautifulSoup(data,"html.parser") 
# print(root.title)
# print(root.title.string)
# titles=root.find("div",class_="title")
# print(titles.a.string)
titles=root.find_all("div",class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)

