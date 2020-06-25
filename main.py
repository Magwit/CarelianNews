from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# import pytest

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

# GIVEN The user is on Karjalainen homepage
driver.get("http://www.karjalainen.fi/")
time.sleep(3)


# WHEN The user clicks on Themes (Sections)


hamburger = driver.find_element_by_id("offcanvas-toggler")

hamburger.click()
time.sleep(1)
# full_screen_themes_xpath = "//a[text()='Teemat']"
# small_screen_themes_xpath = "//li/a[@href='/teemat']"
# cheat_themes_xpath = "/html/body/div[7]/div/div[1]/div/ul/li[4]/a"

time.sleep(1)

# themes = driver.find_element_by_xpath(cheat_themes_xpath)
themes = driver.find_element_by_link_text('TEEMAT')
themes.click()
time.sleep(2)
# Idea . test using different breakpoints
# Idea 2: Use headless browser

# AND the user clicks on the food section
food_section_xpath = "//li/a[text()='Ruoka']"


# THEN The user is at the food section 
food_url = "https://www.karjalainen.fi/teemat/vapaa-aika/ruoka"

article = "//h3[@class='catItemTitle']/a"
# TODO Multiple asserts; the page and the list of articles  

driver.close()
driver.quit()
