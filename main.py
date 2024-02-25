import requests
import sys
from bs4 import BeautifulSoup

link = sys.argv[1]

# Function that retrieves the HTML code for a certain website using the requests library
# Also formats the retrieved HTML code using the prettify() function from the BeautifulSoup library
def websiteHTML():
    r = requests.get(link)
    website_content = r.content
    
    soup = BeautifulSoup(r.content, 'html.parser')  
    
    s = soup.find('div', class_="price")
    content = s.find_all('span')

    print(content)

websiteHTML()
