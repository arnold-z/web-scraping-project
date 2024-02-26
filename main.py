import requests
import sys
from bs4 import BeautifulSoup

# Stores the user's desired search query and website link
search_query = sys.argv[1]
link = sys.argv[2]

# Retrieves the HTML code for a certain website using the requests library
# Formats the retrieved HTML code using the BeautifulSoup library
def priceScraper():
    # GET request
    r = requests.get(link)
    # Retrieves and and parses HTML code
    website_content = r.content
    soup = BeautifulSoup(r.content, 'html.parser') 
    # Finds HTML div with "price" class 
    s = soup.find('div', class_="price")
    # Stores all instances of 'span' element into price_list
    content = s.find_all('span')    

    price_list = []
    
    for c in content:
       price_list.append(c.text)
    # Prints the price of item
    print("The price is: " + price_list[0])

def colorScraper():
    # GET request
    r = requests.get(link)
    # Retrieves and and parses HTML code
    website_content = r.content
    soup = BeautifulSoup(r.content, 'html.parser') 
    # Finds all 'li' elements under the HTMl div where the color should be
    s = soup.find('div', class_="product-details-group-more")
    content = s.find_all('li')
    
    color_list = []

    # Adds all the possible HTML elements that could contain the color into a list
    for c in content:
        color_list.append(c.text)
    
    # Traverses through color_list and finds the text element that contains the color
    for text_elements in color_list:
        # Uses .startswith() function to find the color HTML element
        if (text_elements.startswith('Colorway: ')):
            print(text_elements)
    


if search_query == "-price":
    priceScraper()
elif search_query == "-color":
    colorScraper()