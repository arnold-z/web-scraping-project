import requests
from bs4 import BeautifulSoup


# Function that retrieves the HTML code for a certain website using the requests library
# Also formats the retrieved HTML code using the prettify() function from the BeautifulSoup library
def websiteHTML():
    r = requests.get('https://www.justballgloves.com/product/mizuno-mvp-prime-11-5--baseball-glove--gmvp1151p4/34520/#attr=255076')
    website_content = r.content
    
    soup = BeautifulSoup(r.content, 'html.parser')  
    
    s = soup.find('div', class_="price")
    content = s.find_all('span')

    print(content)

websiteHTML()
