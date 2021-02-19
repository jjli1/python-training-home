import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.google.com/search?q=python3')
soup = BeautifulSoup(r.text, 'lxml')

a_tags = soup.select('ah3')
for tag in a_tags:
    print(tag)
