import time

from pip._internal.operations import check
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    yield driver
    driver.quit()

def test_ghpload(driver):
    pagetitle = driver.title
    assert pagetitle == 'Google','Google Home Page Not loaded'

def test_imagepageload(driver):
    driver.find_element(By.LINK_TEXT,'Images').click()
    pagetitle = driver.title
    assert pagetitle == 'Google Images', 'Images Page Not loaded'

def test_business(driver):
    driver.find_element(By.LINK_TEXT,'Business').click()
    wait = WebDriverWait(driver,10)
    wait.until(EC.title_contains('Business'))
    #assert'Business' in driver.title,'Business Page Not Loaded- Title check'
    #assert'business' in driver.current_url, 'Business Page Not Loaded-URL check'
    check.is_in('Business', driver.title, "Business Page Not Loaded-URL check")
    check.is_in('business',driver.current_url,"Business Page Not Loaded-URL check")

def test_simple_js_alert(driver):
    driver.find_element(By.XPATH, "//button[text()=")