# Project 3

This project expands on my second project and utilizes Beautiful soup.

To run this program, make sure that BeautifulSoup, lxml, html5lib, and requests sre installed. You can do this by running the following command

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
f = open('output.txt', 'w')

f.write("The item you are currently viewing is " +
        product + "and it costs: " + str(price))
f.write("\n" + product + " is made up of " + description + " and comes in: ")
f.write(sizes)
f.write("\n" + shipping + "You also have " + cart +
        " additional item(s) in your cart.")

f.close()  # This is where it writes and saves the file

print("The item you are currently viewing is " +
      product + "and it costs: " + str(price))
print(product + " is made up of " + description + " and comes in: ")
print(sizes)
print("\n" + shipping + "You also have " +
      cart + " additional item(s) in your cart.")

```

When you want to run the script make sure your in the correct folder and then enter the command.
```bash
python scraper.py
```

 Then you should get the name of the item, it's price, what material it's made out of, it's possible sizes, the shipping details, and how many items you have in your cart within the console. This should also create a textfile called output.txt within the same folder and pastes the output.