import requests
import sys
import smtplib
from bs4 import BeautifulSoup

# Stores the user's desired choices for program
search_query = sys.argv[1]
mailScrape = sys.argv[2]
link = sys.argv[3]



# Retrieves the HTML code for a certain website using the requests library
# Formats the retrieved HTML code using the BeautifulSoup library
def priceScraper():
    # GET request
    r = requests.get(link)
    # Retrieves and and parses HTML code
    soup = BeautifulSoup(r.content, 'html.parser') 
    # Finds HTML div with "price" class 
    s = soup.find('div', class_="price")
    # Stores all instances of 'span' element into price_list
    content = s.find_all('span')    

    price_list = []
    
    for c in content:
       price_list.append(c.text)
    # Prints the price of item
    final_price = price_list[0]
    return final_price

def colorScraper():
    # GET request
    r = requests.get(link)
    # Retrieves and and parses HTML code
    soup = BeautifulSoup(r.content, 'html.parser') 
    # Finds all 'li' elements under the HTMl div where the color should be
    s = soup.find('div', class_="product-details-group-more")
    content = s.find_all('li')
    
    color_list = []

    # Adds all the possible HTML elements that could contain the color into a list
    for c in content:
        color_list.append(c.text)
    
    # Traverses through color_list and finds the text element that contains the color
    for color_elements in color_list:
        # Uses .startswith() function to find the color HTML element
        if (color_elements.startswith('Colorway: ')):
            final_color = color_elements
            
    return final_color
    
def sizeScraper():
    # GET request
    r = requests.get(link)
    # Retrieves and and parses HTML code
    soup = BeautifulSoup(r.content, 'html.parser') 
    # Finds all possible instances of size HTML element
    s = soup.find('div', class_="product-details-group-more")
    content = s.find_all('li')

    size_list = []

    for c in content:
        size_list.append(c.text)

    # Traverses possible HTML elements
    # Checks if HTML element contains "Inch Length" and outputs if true
    for size_elements in size_list:
       if "Inch Length" in size_elements:
            final_size = size_elements
            break
    return final_size

def nameScraper():
    # GET request
    r = requests.get(link)
    # Retrieves and and parses HTML code
    soup = BeautifulSoup(r.content, 'html.parser') 
    # Finds all possible instances of name HTML element
    s = soup.find('div', class_="product-details-group description")
    content = s.find_all('strong')

    name_list = []

    # Appends possible HTML elements to name_list
    for c in content:
        name_list.append(c.text)

    # Outputs name of glove
    final_name = name_list[0]
    return final_name

# Stores all web scraping into one variable
def allScraper():
    scrape = "\n" + "Baseball Glove Scraping Information: " + "\n" + nameScraper() + priceScraper() + colorScraper() + "\n" + sizeScraper() + "\n"
    return scrape

# Automatic mail delivery using SMTP library
def mailUpdate():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("webscrapermail@gmail.com", "qiqd fobs rmqc hosz")
    message = allScraper()
    s.sendmail("webscrapermail@gmail.com", "webscrapermail@gmail.com", message)
    s.quit()   

# System arguments that decide output based off user's specifications
if search_query == "-price":
    print(priceScraper())
elif search_query == "-color":
    print(colorScraper())
elif search_query == "-size":
    print(sizeScraper())
elif search_query == "-name":
    print(nameScraper()) 
elif search_query == "-all":
    print(allScraper())
else:
    print("Invalid search query. Please refer to the README file for help.")

# E-mail update conditional
if mailScrape == "-Y":
    mailUpdate()