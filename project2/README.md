# Project 2

I wrote this project because I was really fascinated by Beautiful Soup and wanted to work more with it after completing Lab 8. For this project I just pulled some extra data from their online store and made it all print out to the console. I also checked this with multiple items in their store and it worked everytime.

To run this program, make sure that Python3 is installed and working. As well as BeautifulSoup, lxml, html5lib, and requests. You can do this by running the following command

```bash
pip install bs4 lxml html5lib requests
```
Below is the code that I came up with in order to pull what I believe to be the most useful information from their website.
```bash
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
```

If the url is valid and is the similar to the one in the code(Is the webpage for that single item). Then you should get the name of the item, it's price, what material it's made out of, it's possible sizes, the shipping details, and how many items you have in your cart.