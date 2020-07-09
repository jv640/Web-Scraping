import requests 
from bs4 import BeautifulSoup
import html5lib as h5l
count = 1
while 1:
    r = requests.get("http://www.hotstar.com")
    print(count)
    count = count + 1
