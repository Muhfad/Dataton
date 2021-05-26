#!/usr/bin/python3

'''
---------------------------------------------------------
author: Muhammed Fadera
date: 27/01/2021
task: this script fetches data on the trending videos on youtube
      using selenium
'''

# load required dependencies
import fuckit
from selenium.webdriver import Firefox # for opening the browsing
from selenium.webdriver.firefox.options import Options # for setting options
from selenium.webdriver.common.by import By # search using different methods
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys # for interfacing with the keyboard
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pandas as pd
from numpy import nan as NA
import re
# import utilities as utils
import time
# from utilities import EMAIL, PASSWORD



'''
utility functions: I tried putting this in their own scrip but for some reason
runs fine in that script but when I import it doesnt.
'''
utility = True
if utility:
    '''
    this is a copy of the code in the utilities.py file
    '''
    # GLOBAL VARIABLES
    LIKES = 17 # location of the 'like' button
    DISLIKES = 19 # location of the 'dislike' button
    text_to_num_dict = {
    'M':1e6, 'K':1e3, 'B':1e9
    }

    text_to_num_dict = {
    'M':1e6, 'K':1e3, 'B':1e9
    }
    # xpath to comment
    comments_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/'
    comments_xpath += 'div[6]/div[3]/ytd-video-secondary-info-renderer/div/'
    comments_xpath += 'ytd-expander/div/div/yt-formatted-string/span[2]/text()'

    # xpath to whether or not the channel is official
    verified_xpath = '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/'
    verified_xpath += 'div[5]/div[1]/div/div[6]/div[3]/ytd-video-secondary-info-renderer/div'
    verified_xpath += '/div[2]/ytd-video-owner-renderer/div[1]/ytd-channel-name/ytd-badge-supported-renderer/div'

    def from_text_to_num(x):
        '''
        converts a text of the form for example '1K' to 1000
        '''
        global text_to_num_dict
        factor = 1
        x = re.sub(r',', '', x)
        for suffix in text_to_num_dict:
            if x.endswith(suffix):
                factor = text_to_num_dict[suffix]
                break
        y = re.sub(r',|(\s*[a-zA-Z]*\s*)$', '', x)
        y = float(y) * factor if len(y) != 0 else 0
        return y

    def scroll_down_up():
        '''
        this scrolls a web page up and down to activate its elements using the
        firefox shortcuts ctrl + up for going to top of the page and ctrl + down
        to go to the bottom
        '''
        time.sleep(10)
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.CONTROL + Keys.DOWN)
        time.sleep(10)
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.CONTROL + Keys.DOWN)
        time.sleep(10)
        return True

    def login(driver):
        '''
        this logs into gmail and makes the process of scraping data a less tedious
        '''
        login_link = 'https://accounts.google.com/signin/v2/identifier?hl=en-GB'
        login_link += '&continue=https%3A%2F%2Fwww.google.com%2F%3Fgws_rd%3Dssl&gae='
        login_link += 'cb-&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
        driver.get(login_link)
        # initialized action
        action = ActionChains(driver)

        # search box finder
        search = driver.find_element_by_css_selector('#identifierId')
        driver.implicitly_wait(15)
        search.send_keys(EMAIL + Keys.ENTER)
        search = driver.find_element_by_css_selector('#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
        driver.implicitly_wait(15)
        search.send_keys(PASSWORD + Keys.ENTER)

    def find_comments():
        '''
        this functions checks if the current loaded elements contains the comments
        and the extracts it
        '''
        vid_comments = None
        # driver.find_element_by_xpath(comments_xpath).click().send_keys(Keys.DOWN)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#description > yt-formatted-string > span:nth-child(1)'))).click()
        time.sleep(10)
        # wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.CONTROL + Keys.UP)
        try:
            vid_comments = from_text_to_num(wait_comments.until(EC.presence_of_element_located((By.XPATH, comments_xpath))).text)
        except:
            pass
        return vid_comments





#------------------------------------------------------------------------------#
# executable location and the base link to be scrape
wbdriver_path = '/home/muhammed/wbdtools/geckodriver/geckodriver'
urlpage = 'https://www.youtube.com/feed/trending'

# setting options for the browser
options = Options()
options.headless = True # should prevent browser window from opening
options.add_argument("window-size=1280,800")


#start timing
t1 = time.time()

# opening browser
driver = Firefox(options=options, executable_path=wbdriver_path)
# this should prevent a site from detecting that you are using a bot
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.get(urlpage)
time.sleep(15)
driver.maximize_window()

driver.execute_script("window.scrollTo(0, 1500);")
time.sleep(15)
# maximize window
# setup a wait, this can be use whenever you
# need to let the browser finish loading
wait = WebDriverWait(driver, 10)
# wait_comments = WebDriverWait(driver, 10000) # comments seems to take longer to load
# sanity check
driver.title



#------------------------------------------------------------------------------#
# task
# all the videos
vids_names = driver.find_elements_by_xpath('//*[@id="video-title"][@class="yt-simple-endpoint style-scope ytd-video-renderer"]')
p = vids_names[0]
vids_links = []

for i in vids_names:
    vids_links.append(i.get_attribute('href'))


print('%s has %d videos'%(driver.title, len(vids_links)))

# dataframe to store collected data
df = pd.DataFrame(columns = ['ID', 'title', 'description', 'Verified', 'subcount',
                             'viewcount', 'channel_name', 'date_uploaded',
                             'likes', 'dislikes', 'upvotes', 'rank'])

# exit code for whether or not the login screen has been bypass
exit_code = 0
vid_rank = 0
count = 0
start_time = time.ctime()
# fuckit will execute the code irrepective of any error
# there are situation in which this is desired.
# for example when you keep gettting an exception even
# after using a try/except block
try:
    for x in vids_links:
        driver.get(x) # search link
        # skips login screen
        # it only has to do this on the first video
        if vid_rank == 0:
            try:
                time.sleep(15)
                driver.find_element_by_css_selector('yt-formatted-string.yt-button-renderer:nth-child(1)').click()
                try:
                    time.sleep(5)
                    driver.find_element_by_css_selector('#introAgreeButton').click()
                except:
                    pass
            except:
                pass


        # scrolls webpage to activate elements
        time.sleep(30)
        driver.execute_script("window.scrollTo(0, 1500);")
        time.sleep(20)


        # title of video
        vid_id = x.strip('https://www.youtube.com/watch?v=')

        # title of video
        vid_title = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#container > h1 > yt-formatted-string"))).text

        # description of video
        try:
            vid_desc = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#description > yt-formatted-string > span:nth-child(1)"))).text
        except:
            vid_desc = vid_title


        # is the channel Verified
        verified = False
        try:
            driver.find_element_by_xpath(verified_xpath)
            verified = True
        except:
            pass
        # number of subs
        vid_subs = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#owner-sub-count"))).text.strip(' subscibers')
        vid_subs = from_text_to_num(vid_subs)

        # number of views
        vid_views = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#count > yt-view-count-renderer > span.view-count.style-scope.yt-view-count-renderer")))
        vid_views = from_text_to_num(vid_views.text)

        # name of channel
        vid_channel = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#text > a"))).text

        # date the video was uploaded
        vid_date = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#date > yt-formatted-string"))).text

        # extracting the number of likes and number of dislikes
        all_buttons = driver.find_elements_by_css_selector('#button')
        like_button = all_buttons[LIKES]
        dislike_button = all_buttons[DISLIKES]

        # likes
        vid_likes = like_button.get_attribute('aria-label')
        vid_likes = ''.join(re.findall(r'\d+', vid_likes))
        vid_likes = int(vid_likes) if len(vid_likes) != 0 else 0
        # dislikes
        vid_dislikes = dislike_button.get_attribute('aria-label')
        try:
            vid_dislikes = ''.join(re.findall(r'\d+', vid_dislikes))
        except:
            vid_dislikes = ''
        vid_dislikes = int(vid_dislikes) if len(vid_dislikes) != 0 else 0



        # rank on trending
        vid_rank = vid_rank + 1
        # vid_rank = wait.until(EC.presence_of_element_located(
        # (By.XPATH, '//*[@id="container"]/yt-formatted-string/a'))).text
        #
        # vid_rank = int(vid_rank.strip('#').strip('ON TRENDING'))
        # update dataframe

        # number of upvotes
        try:
            vid_upvotes = sum([from_text_to_num(i.text) for i in driver.find_elements_by_css_selector('#vote-count-middle')])
        except:
            vid_upvotes = NA
        df.loc[len(df)] = [vid_id, vid_title, vid_desc, verified, vid_subs,
                           vid_views, vid_channel, vid_date, vid_likes,
                           vid_dislikes, vid_upvotes, vid_rank]
        print(count, 'done', sep=' ')
        count += 1
except:
    driver.quit()


df['timestamp'] = start_time + ' to ' + time.ctime()
file_path = 'data/' + start_time + '.csv'
df.to_csv(file_path)
print('Finished in %s'%(time.time() - t1))
