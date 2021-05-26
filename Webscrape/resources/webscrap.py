# loading libraries
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

'''
introduction to webscraping
source of resource
https://www.analyticsvidhya.com/blog/2019/05/scraping-classifying-youtube-video-data-python-selenium/
'''
# setting the options for the webpage
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

# setting up firefox drivers
wbdriver_path = '/home/muhammed/wbdtools/geckodriver/geckodriver'
urlpage = 'https://www.youtube.com/feed/trending'
driver = webdriver.Firefox(options=options, executable_path=wbdriver_path)
driver.get(urlpage)
# up and down scrol to activate webpage
# driver.execute_script(
#     "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;"
#     )
# sleep for 30s
# time.sleep(30)
# driver.quit()

driver.title

vids_names = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []

for i in vids_names:
    links.append(i.get_attribute('href'))

print(links)

df = pd.DataFrame(columns = ['link', 'title', 'description', 'category'])
wait = WebDriverWait(driver, 10)
v_category = "trending"
for x in links:
    driver.get(x)
    v_id = x.strip('https://www.youtube.com/watch?v=')
    v_title = wait.until(EC.presence_of_element_located(
                   (By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
    v_description =  wait.until(EC.presence_of_element_located(
                                 (By.CSS_SELECTOR,"div#description\
                                  yt-formatted-string"))).text
    df.loc[len(df)] = [v_id, v_title, v_description, v_category]


df.head()
