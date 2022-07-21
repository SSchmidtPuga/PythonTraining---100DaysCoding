from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


chrome_driver_path = "/Applications/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("http://secure-retreat-92358.herokuapp.com/")


# data = driver.find_element_by_id("articlecount").text
# print(data)
#
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()

search1 = driver.find_element_by_name("fName")
search1.send_keys("Sebastian")

search2 = driver.find_element_by_name("lName")
search2.send_keys("Schmidt")

search3 = driver.find_element_by_name("email")
search3.send_keys("seschmidt@alumnos.uai.cl")
search3.send_keys(Keys.ENTER)

button = driver.find_elements_by_class_name("btn btn-lg btn-primary btn-block")
button.click()


driver.close()
driver.quit()