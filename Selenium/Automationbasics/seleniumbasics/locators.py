import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Edge()
driver.get("https://www.google.com")
time.sleep(3)


#ID
'''search_input = driver.find_element(By.ID,"APjFqb")
search_input.send_keys("selenium")
time.sleep(3)
search_input.clear()
time.sleep(2)
#Name
search_input = driver.find_element(By.NAME,"q")
search_input.send_keys("locators")
time.sleep(3)
#Name
googlesearch_button = driver.find_element(By.NAME,"btnK")
googlesearch_button.click()
time.sleep(30)

#ClassName
imfl_button = driver.find_elements(By.CLASS_NAME, "RNmpXc")
imfl_button.click()
time.sleep(3)

#Tagname
href_elements = driver.find_elements(By.TAG_NAME,"a")
for elmt in href_elements:
    print(f'{elmt.text} - {elmt.get_attribute("href")}')
driver.quit()

#Linktext
images_link = driver.find_element(By.LINK_TEXT,"Images")
images_link.click()
time.sleep(10)'''

#CSSsel
search_input = driver.find_element(By.CSS_SELECTOR,'div > textarea')
search_input.send_keys('selenium')
time.sleep(5)
settings_text = driver.find_element(By.XPATH,"")
print(settings_text.text)
time.sleep(3)

#AND & OR expressions
and_example = driver.find_element(By.XPATH,"//td[text()='Tim' and @class='first-name']")
print(f"AND Example -> Found with  conditions: {and_example.text}")
or_example = driver.find_element(By.XPATH,"//td[text()='Tim' or text()='Frank']")
print(f"AND Example -> Found with OR conditions: {or_example.text}")

#Child=select
rows = driver.find_elements(By.XPATH, "//table[@id='table1'/tbody/tr/td")
print(f"Child Example -> Found{len(rows)} columns in the first table.")

#Parent- get the parent row of a particular cell
email_cell = driver.find_element(By.XPATH, "//table[@id='table']")


#Ancestor - get the table element that is an anestor of a cell
ancestor_table = driver.find_element(By.XPATH,"//td[text()='jsmith@gmail.com']/ancestor::table:")
print(f"Ancestor Example -> Table ID: {ancestor_table.get_attribute('id')}")

descendants = driver.find_element(By.XPATH,"//table[@id='table1']/descendant::td")
print(f"Descendant Example -> Found {len(descendants)} descendant cells.")

'''#RELATIVE LOCATOR

driver.get("https://www.saucedemo.com")
time.sleep(2)

#Elements used for reference
username_field = driver.find_element(By.ID,"user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID,"login-button")

#above -> element located above another
elmt_above_password = driver.find_element(locate_with(By.TAG_NAME,"input").above(password_field))
elmt_above_password.send_keys('standard_user')
time.sleep(5)

#below -> element located below another
field_below_username = driver.find_element(
    locate_with(By.TAG_NAME,"input").below(username_field))
print(f"Below Example -> Placeholder below username:  {field_below_username}" )
field_below_username.send_keys('secret_sauce')
time.sleep(2)

login_button.click()
time.sleep(5)

#toRight -> element to the left of another
twitter_icon = driver.find_element(By.LINK_TEXT,"Twitter")
facebook_icon = driver.find_element(locate_with(By.TAG_NAME,"a").to_right_of(twitter_icon))
print(f"to leftOf Example Element to the left of Twitter icon has href:{facebook_icon.get_attribute("href")}")
left_icon = driver.find_element(locate_with(By.TAG_NAME,"a").to_left_of(facebook_icon))
print(f"toRightOf Example Element to the right of Twitter icon has href:{facebook_icon.get_attribute("href")}")
near_twitter = driver.find_element(locate_with(By.TAG_NAME,"a").near(twitter_icon))
print(f"toRightOf Example Element to the right of Twitter icon has href:{facebook_icon.get_attribute("href")}")
time.sleep(3)'''













driver.quit()
