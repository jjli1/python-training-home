import requests

my_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'}


r = requests.get('https://www.google.com/search?q=python2')
r.encoding = 'big5'
print(r.content)
# print(r.headers)
# print(r.headers['Date'])
# print(r.content.decode())
# for header in r.headers:
#     print(header)
# with open('./searchHTML.html', 'w+') as f:
#     f.write(r.text)
print(r.text)
