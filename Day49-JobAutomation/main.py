from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import warnings
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, JavascriptException

warnings.filterwarnings("ignore", category=DeprecationWarning)

chrome_driver_path = "/Applications/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(" https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")


log_in = driver.find_element_by_partial_link_text("Iniciar sesión")
log_in.click()




username = driver.find_element_by_id("username")
username.send_keys("spuga123@gmail.com")


password = driver.find_element_by_id("password")
password.send_keys("Ss12721272!!")
password.send_keys(Keys.ENTER)


all_listings = driver.find_elements_by_css_selector(".jobs-search-results li")

for jobs in all_listings:
    jobs.click()
    time.sleep(0.1)
    try:
        save = driver.find_element_by_class_name("jobs-save-button")
        save.click()
        driver.execute_script("""
           var l = document.getElementsByClassName("artdeco-toasts_toasts")[0];
           l.parentNode.removeChild(l);
        """)

        time.sleep(0.1)

    except NoSuchElementException and JavascriptException :
        print("No application button, skipped.")
        continue









