from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pytest

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

# GIVEN The user is on Karjalainen homepage
driver.get("http://www.karjalainen.fi/")
time.sleep(3)


# WHEN The user clicks on Themes (Sections)
themes_xpath = "//a[text()='Teemat']"
# AND the user clicks on the food section
food_section_xpath = "//li/a[text()='Ruoka']"


# THEN The user is at the food section 
food_url = "https://www.karjalainen.fi/teemat/vapaa-aika/ruoka"

article = "//h3[@class='catItemTitle']/a"
# TODO Multiple asserts; the page and the list of articles  

driver.close()
driver.quit()
