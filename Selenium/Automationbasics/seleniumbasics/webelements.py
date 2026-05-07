import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
#Start driver
driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

time.sleep(1)
#TEXT INPUT
text_input = driver.find_element(By.ID,"my-text-id")
text_input.clear()
text_input.send_keys("Selenium WebDriver Demo")
time.sleep(3)
#PASSWORD INPUT
password_input = driver.find_element(By.NAME,"my-password")
password_input.clear()
password_input.send_keys("secret123")
time.sleep(3)
#TEXT AREA
text_area = driver.find_element(By.NAME,"my-textarea")
text_area.clear()
text_area.send_keys("This is a sample message")

time.sleep(3)

#CHECKBOX
checkbox = driver.find_element(By.ID,"my-check-2")
checkbox.click()

#RADIO
radio = driver.find_element(By.ID,"my-radio-2")
radio.click()

#DROPDOWN
dropdown = driver.find_element(By.NAME,"my-select")
dropdown.click()

option = driver.find_element(By.CSS_SELECTOR,"select[name='my-select'] option[value='2']")
option.click()

#MULTI-SELECT
mutli_select = driver.find_element(By.NAME,"my-datalist")
mutli_select.send_keys('New York')
#FILE UPLOAD
file_upload = driver.find_element(By.NAME,"my-file")
file_upload.send_keys("C:\\Users\\wprjavanguser\\Downloads\\ChromeSetup.exe")
#RANGE
range_slider = driver.find_element(By.NAME,"my-range")
driver.execute_script("arguments[0].value= 10;", range_slider)

#COLOR PICKER
color_picker = driver.find_element(By.NAME,"my-colors")
color_picker.send_keys("#00ff00")
#DATE PICKER
data_input = driver.find_element(By.NAME,"my-date")


driver.quit()

