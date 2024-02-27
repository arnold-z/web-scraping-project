# Baseball Glove Web Scraper ⚾️
Python script that searches for a baseball's glove features from "justballgloves.com"

## Dependencies

- [requests](https://pypi.org/project/requests/)
```
pip install requests
```
- [smtplib](https://docs.python.org/3/library/smtplib.html)

**Edit line 875 of your smtp library to ```msg = _fix_eols(msg).encode('utf-8')```**
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

### Second argument (email feature)
To send automatic emails, do:
```
-Y
```
To opt out, do:
```
-N
```

### Third argument (user's desired email)
If you chose "-Y" above, input:
```
*insert desired email*
```

If you chose "-N" above, input:
```
-N
```

### Fourth argument (link)
To specify which justballgloves.com link, do:
```
*insert link here*
```

### Examples
```
python main.py -all -Y *insert email here* *insert justballgloves.com link here*
```
```
python main.py -price -N -N *insert justballgloves.com link here*
```


  
