from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
url = 'https://www.imdb.com/list/ls561448893/?ref_=otl_1'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

