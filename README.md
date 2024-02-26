# Baseball Glove Web Scraper ⚾️
Program that searches for a baseball's glove features from "justballgloves.com"

## Dependencies

- [requests](https://pypi.org/project/requests/)
```
pip install requests
```
- [sys](https://docs.python.org/3/library/sys.html)

- [smtplib](https://docs.python.org/3/library/smtplib.html)

```
pip install smtplib
```
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
```
pip install BeautifulSoup
```

## Commands and Arguments to Run

### First argument (scrape choice)

To only scrape the price, do:
```
-price
```

To scrape the glove color, do:
```
-color
```

To scrape the size, do:
```
-size
```

To scrape the name, do:
```
-name
```

To do all, do:
```
-all
```

### Second argument (email)
To send automatic emails, do:
```
-Y
```

### Third argument (link)
To specify which justballgloves.com link, do:
```
*insert link here*
```

### Examples
```
python main.py -all -Y https://www.justballgloves.com/product/wilson-a2000-1786-11-5--baseball-glove--wbw100390115/34681/#attr=255502
```

  
