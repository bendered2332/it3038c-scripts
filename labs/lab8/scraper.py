import requests
import re
from bs4 import BeautifulSoup

data = requests.get(
    "https://www.sparktrendz.com/products/aki-black-shorts").content
soup = BeautifulSoup(data, 'html.parser')
div = soup.find('span', class_='current_price').text.strip()
#div = soup.find('div', class_="price__container price__container--display-price-true has-margin-right").text

product = soup.find('h1', class_='product_name').text

print(div)

print(product)

print("The item you are currently viewing is " +
      product + "and it costs: " + str(div))
