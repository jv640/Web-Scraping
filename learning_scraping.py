import requests 
from bs4 import BeautifulSoup
import html5lib as h5l

url = "https://youtube.com"

    # Get the HTML using URL

r = requests.get(url)
htmlContent = r.content
    # print(htmlContent)

    # Now parse the content
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup)
print(soup.prettify)

    # Travelling the tree
    # commonly used types of objects of soup

    # type 1 Tag
print(soup.title)       # Printing Title of page
print(type(soup.title))
    # type 2 Naivigable String
print(soup.title.string)       # Printing Title of page
print(type(soup.title.string))
    # type 3 BeautifulSoup
print(soup)       # Printing Title of page
print(type(soup))

    #Get all paragraphs

paras = soup.find_all('p')
print(paras)

    #Get all the Anchors
anchors = soup.find_all('a')
print(anchors)

    #Getting first paragraph
print(soup.find('p'))

    #Getting first anchor
print(soup.find('a'))

    # Get classes of any tag    (if class or id will not be present then it will give key error)
print(soup.find('a')['class'])
    # Get ID of any tag
print(soup.find('a')['id'])

    #Get all anchro element with given class
print(soup.find_all("a", class_ = "spf-link"))

    #get text form elements
print(soup.find('p').get_text())
print(soup.get_text())

    # getting link of all anchor tags
for link in anchors:
    print(link.get('href'))
    # to make those link clickable just add base url in front 

