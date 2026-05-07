
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = input('What browser do you want to use?').lower()

match (browser):
    case 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    case 'edge':
        driver = webdriver.Edge(service=Service("../resource/msedgedriver.exe"))
    case _:
        print('Unknown browser - Not available.\n Executing with default EDGE browser.')



driver.get("https://www.google.com")



pagetitle = driver.title

if pagetitle =='Google':
    print("Google Homepage loaded-Pass")
else:
    print("Google HomepageNot loaded - Fail")



driver.quit()




