from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Applications/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")


data = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul')

#
driver.close()
driver.quit()
