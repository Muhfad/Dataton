'''
- contains utility functions for cleaning and parsing some data structures
- contains the definition/value of GLOBAL VARIABLES
'''

import re
import os


# GLOBAL VARIABLES
LIKES = 17 # location of the 'like' button
DISLIKES = 19 # location of the 'dislike' button
text_to_num_dict = {
'M':1e6, 'K':1e3, 'B':1e9
}

text_to_num_dict = {
'M':1e6, 'K':1e3, 'B':1e9
}



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

def scroll_up_down(driver):
    '''
    this scrolls a web page up and down to activate its elements
    '''
    driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;"
    )
    time.sleep(15)
    return

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
