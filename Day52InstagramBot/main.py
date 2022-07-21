
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import warnings
import time
warnings.filterwarnings("ignore", category=DeprecationWarning)

chrome_driver_path = "/Applications/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.instagram.com/")

instagram_account = "juanpisgonzalez"
username = "ecommersespana@gmail.com"
password = "Ss12721272!!"
# -------------------------------------------Log in  -------------------------------------------------------------------

time.sleep(3)
username2 = driver.find_element_by_css_selector("input[name='username']")
username2.send_keys(username)

password2 = driver.find_element_by_css_selector("input[name='password']")
password2.send_keys(password)
password2.send_keys(Keys.ENTER)

time.sleep(3)
not_now = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
not_now.click()

time.sleep(3)
not_notify = driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
not_notify.click()


instagram_account2 = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
instagram_account2.send_keys(instagram_account)
time.sleep(6)
instagram_account2.send_keys(Keys.ENTER)
instagram_account2.send_keys(Keys.ENTER)


# -------------------------------------------follow -------------------------------------------------------------------
time.sleep(6)
followers = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
followers.click()
time.sleep(2.5)

buttons = 0

all_buttons = driver.find_elements_by_css_selector(".PZuss li button")
for button in all_buttons:
    drop_down = 0
    button.click()
    buttons +=1
    time.sleep(3)
    if buttons %3 == 0:
        modal = driver.find_element_by_css_selector("ul.jSC57 li:last-child div")
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(2)







# ElementNotInteractableException