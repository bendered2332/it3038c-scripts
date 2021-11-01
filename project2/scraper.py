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

# Pulls the fabric type
div = soup.find('div', class_='description bottom')
description = div.ul.li.span.text
# print(description)

# Pulls the shipping information about the product
div = soup.find('div', class_='description bottom')
shipping = div.strong.text
# print(shipping)

# Pulls the current amount of items you have in your cart
cart = soup.find('div', class_='cart-container').text.strip()
# print(cart)

# Pulls the different sizes for the product
sizes = soup.find('div', class_='swatch is-flex is-flex-wrap').text.strip()
# print(sizes)

# Prints the item name and cost
print("The item you are currently viewing is " +
      product + "and it costs: " + str(price))
print(product + " is made up of " + description + " and comes in: ")
print(sizes)
print(shipping + "You also have " + cart + " additional item(s) in your cart.")
