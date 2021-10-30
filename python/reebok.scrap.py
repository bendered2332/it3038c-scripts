import requests
import re
from bs4 import BeautifulSoup

data = requests.get(
    "https://www.microcenter.com/product/635448/powerspec-g509-gaming-pc").content
soup = BeautifulSoup(data, 'html.parser')
details = soup.find("h1")
for d in details:
    title = d.find("span", {"class": re.compile('ProductLink.*')})
    print(title)
