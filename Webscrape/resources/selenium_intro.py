'''
introduction to Selenium
source: selenium documentation
'''

from selenium.webdriver import Firefox # for the main workhorse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


# setup
wbdriver_path = '/home/muhammed/wbdtools/geckodriver/geckodriver'
urlpage = 'https://www.youtube.com/feed/trending'
# setting page loading strategy
options = Options()
# this waits for the browser to load all
# required elements like styles and html
options.page_load_strategy = 'eager'
# urlpage = 'https://seleniumhq.github.io'
driver = Firefox(executable_path=wbdriver_path)

## (1) BASIC WEB ACTIONS
# open web browser
driver.get(urlpage)
# current url
driver.current_url
# press back button
driver.back()
# press forward button
driver.forward()
# refresh
driver.refresh()
# title of current page
driver.title

## (2) WINDOWS AND TABS
# each window has a unique identifier
driver.current_window_handle
# all windows
driver.window_handles
# switching windows or tabs
with Firefox(executable_path=wbdriver_path) as driver:
    # Open URL
    driver.get(urlpage)

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Check that no other window is open
    assert len(driver.window_handles) == 1

    # click the link which opens in a new window
    Odegaard = 'Welcome to The Arsenal, Martin Odegaard | First Interview' # name of the link to open
    driver.find_element(By.LINK_TEXT, 'Welcome to The Arsenal, Martin Odegaard | First Interview').click()

    # Wait for the new window/window
    wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading
    wait.until(EC.title_contains('Welcome to The Arsenal'))


# Create a new window and switch to it
# tab
Odegaard = 'Welcome to The Arsenal, Martin Odegaard | First Interview'
driver.switch_to.new_window(Odegaard)
# close the tab or window
driver.close()
# switch back to original tab or window
original_window = driver.current_window_handle
driver.switch_to.window(original_window)

# quit browser at the end of session
driver.quit()
# you can include all of this in a try/finally block

## (3) WINDOW MANAGEMENT
# getting window size
width = driver.get_window_size('width')
height = driver.get_window_size('height')
size = driver.get_window_size()
width1 = size.get('width')
height1 = size.get('height')

# maximize/minimize/full screen
driver.maximize_window()
driver.minimize_window()
driver.fullscreen_window()

# take a screenshot!
driver.save_screenshot('./trending.png')

# screenshot by webElement
el = driver.find_element(By.TAG_NAME, 'head')
el.text
# title.screenshot('./title.png')
# Print a page
# from selenium.webdriver.common.print_page_options import PrintOptions


## (4) WEB ELEMENTS
# WebElement represents a DOM element. WebElements can be
# found by searching from the document root using a
# WebDriver instance, or by searching under another WebElement.

# find_element: finds the first match of an element and return it
# throws a NoSuchElementException error when no match is found
head = driver.find_element(By.TAG_NAME, "head")

# find_elements: returns list of all matches
# returns an empty list when no match is found
div_tags = driver.find_elements(By.TAG_NAME, "div")
p_tags = driver.find_elements(By.TAG_NAME, 'p')
len(div_tags)
div_tags[1000].text
len(p_tags)
try:
    ibra = driver.find_element(By.NAME, 'zlatan')
except:
    pass

# find elements within elements
div_2 = div_tags[0].find_elements(By.TAG_NAME, 'div')
div_2[0].text


# the element which has focus in the browser
driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys('webElement')
# fins the cordinate of the reference element
div_2[0].rect

# get css value
cssValue = driver.findElement(By.LINK_TEXT, \
                  "Tommy Makes Rust 1000\% Funnier").value_of_css_property('color')


## (5) SENDING KEYSTROKES
# typing into text boxes
from selenium.webdriver.common.keys import Keys
driver.get('http://www.google.com')
# enter the text frank lampard and then perfom the 'ENTER' keyboard action
search = driver.find_element(By.NAME, "q")
search.send_keys("frank lampard" + Keys.ENTER)
# simulate keypresses (CONTROL, SHIFT, ALT) := this are called keydowns
# think of it as a key press
from selenium import webdriver
webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
# key releases
action = webdriver.ActionChains(driver)
# Enters text "qwerty" with keyDown SHIFT key and after keyUp SHIFT key (QWERTYqwerty)
action.key_down(Keys.SHIFT).send_keys_to_element(search,
                "qwerty").key_up(Keys.SHIFT).send_keys("qwerty").perform()


# clears the search box
search.clear()
