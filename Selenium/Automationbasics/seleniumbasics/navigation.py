import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Edge()



driver.get('https://www.google.com')

time.sleep(3)
driver.get('https://www.wikipedia.com')
time.sleep(3)

driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.back()
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.quit



