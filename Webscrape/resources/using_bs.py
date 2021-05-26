'''
scraping youtube using BeautifulSoup
source of resource
https://medium.com/analytics-vidhya/scraping-youtube-video-with-beautifulsoup-python-d30598285965
'''

from bs4 import BeautifulSoup # for scraping
import requests               # requered for reading the files
import pandas as pd           # for dataframes
import json                   # export output to json
import os
from urllib.request import urlopen

# AC Milan vs Inter
url = 'https://www.youtube.com/watch?v=0NqBmCcI1sM'
Vid = {}
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')

soup.get_text()
