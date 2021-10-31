import requests
import re
from bs4 import BeautifulSoup

data = requests.get(
    "https://www.sparktrendz.com/products/aki-black-shorts").content
soup = BeautifulSoup(data, 'html.parser')

# Pulls the item cost and strips it of any whitespace
price = soup.find('span', class_='current_price').text.strip()

# Pulls the item name
product = soup.find('h1', class_='product_name').text

# Prints the item name and cost
print("The item you are currently viewing is " +
      product + "and it costs: " + str(price))
