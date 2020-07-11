import requests 
from bs4 import BeautifulSoup
import html5lib as h5l
count = 1

r = requests.get("https://www.iplt20.com/archive/2018/01")
print(r.history)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')

