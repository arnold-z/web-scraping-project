# Baseball Glove Web Scraper ⚾️
Python script that searches for a baseball's glove features from "justballgloves.com"

## Dependencies

- [requests](https://pypi.org/project/requests/)
```
pip install requests
```
- [smtplib](https://docs.python.org/3/library/smtplib.html)

```
pip install smtplib
```
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
```
pip install BeautifulSoup
```
- [sys](https://docs.python.org/3/library/sys.html) (Downloaded with Python)

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
To opt out, do:
```
-N
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
```
python main.py -price -Y https://www.justballgloves.com/product/wilson-a2000-1786-11-5--baseball-glove--wbw100390115/34681/#attr=255502
```


  
