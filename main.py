from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pytest

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://repl.it/@SergeiChestakov/selenium")
driver.get("http://www.karjalainen.fi/")
time.sleep(3)
driver.close()
driver.quit()
