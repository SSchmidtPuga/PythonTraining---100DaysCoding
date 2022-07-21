from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import warnings
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, JavascriptException, \
    ElementNotInteractableException

warnings.filterwarnings("ignore", category=DeprecationWarning)

chrome_driver_path = "/Applications/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(" https://www.speedtest.net/es")

try:
    start = driver.find_element_by_css_selector(".start-button a ")
    start.click()
    time.sleep(40)
    delete_button = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a")
    delete_button.click()
    download_speed = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
    download_speed = int(download_speed.split(".")[0])
    if download_speed < 600:
        driver.get(" https://twitter.com/home")
        time.sleep(12)
        username = driver.find_element_by_name("username")
        username.send_keys("spuga123@gmail.com")
        username.send_keys(Keys.ENTER)
        time.sleep(2)

        try:
            phone = driver.find_element_by_css_selector(
                "input[name='text'")
            phone.send_keys("Sebasti52606190")
            phone.send_keys((Keys.ENTER))
            time.sleep(1)

            password = driver.find_element_by_name("password")
            password.send_keys("Ss12721272!!")
            password.send_keys((Keys.ENTER))
            time.sleep(4)

            twit = driver.find_element_by_xpath(
                "/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
            twit.send_keys("Mother fucker")

        except NoSuchElementException:
            password = driver.find_element_by_name("password")
            password.send_keys("Ss12721272!!")
            password.send_keys((Keys.ENTER))
            time.sleep(1)

except NoSuchElementException and ElementNotInteractableException:
    print("no found")



