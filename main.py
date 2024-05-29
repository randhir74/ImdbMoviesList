# If you want to scrape a website
# Use the API
# HTML web scraping using some tool like bs4

# Step - 0 = Install all the requirements

# pip install requests
# pip install bs4
# pip install html5lib

from turtle import title
import requests
from requests import get
from bs4 import BeautifulSoup
url = "https://www.javatpoint.com/computer-network-architecture"

#Step 1 : Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2 : Parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

#Step 3 : Html Tree traversal
title = soup.title
print(type(title.string))

#Commonly used types of objects:
#1. Tag
#2. NavigableString
#3