from bs4.element import PageElement
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# commonly used types of objects:
# 1.tag print(type(title))
# 2.navigableString print(type(title. string))
# 3.beautifulsoup print(type(soup))
# 4.comment   markup = "<p><!--this is a comment --</p>"soup2 = BeautifulSoup(markup)print(soup2.p.string)


# get the title of html page
title = soup.title


# get all the paragraph from the Page
paras = soup.find_all('p')
# print(paras)
# get first element in html page
print(soup.find('p'))
# get classes of any element
print(soup.find('p')['class'])
# get text from elements
print(soup.find('p').get_text())

# get all anchors tag
anchors = soup.find_all('a')
all_links = set()
# get all links on page:
for link in anchors:
    if(link.get('href') != '#'):
        linkText = ("http://codewithharry.com" + link.get('href'))
        all_links.add(link)
        print(linkText)

# .contents-  A tags children are available as a list
# .children-A tags children are available as a generator

navbarSupportedContent = soup.find(id='navbarSupportedContent')
# for elem in navbarSupportedContent.contents:
# print(elem)
# for item in navbarSupportedContent.strings:
# print(item)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

elem = soup.select('#loginModal')
print(elem)
