import requests
import sys
from bs4 import BeautifulSoup

# Stores the user's desired website link
search_query = sys.argv[1]
link = sys.argv[2]

# Retrieves the HTML code for a certain website using the requests library
# Formats the retrieved HTML code using the BeautifulSoup library
def priceScraper():
    r = requests.get(link)
    website_content = r.content
    soup = BeautifulSoup(r.content, 'html.parser')  
    s = soup.find('div', class_="price")
    content = s.find_all('span')    

    price_list = []

    for c in content:
       price_list.append(c.text)
   
    print(price_list[0])

if search_query == "-price":
    priceScraper()