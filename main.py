import requests
from bs4 import BeautifulSoup


# Function that retrieves the HTML code for a certain website using the requests library
# Also formats the retrieved HTML code using the prettify() function from the BeautifulSoup library
def websiteHTML():
    r = requests.get('https://stockx.com/nike-kyrie-5-spongebob-pineapple-house')
    website_content = r.content
    
    soup = BeautifulSoup(r.content, 'html.parser')  
    return soup.prettify()
