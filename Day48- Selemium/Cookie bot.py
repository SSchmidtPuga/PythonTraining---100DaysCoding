from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import warnings
import time
warnings.filterwarnings("ignore", category=DeprecationWarning)


chrome_driver_path = "/Applications/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")

timeout = time.time() +60*5



while 3>0:
    cookie = driver.find_element_by_id("bigCookie")
    cookie.click()
    upgrades = driver.find_element_by_id("products")
    upgrades.click()
