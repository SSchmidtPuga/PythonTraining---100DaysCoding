from bs4 import BeautifulSoup
import lxml
import requests




headers = {
    "Accept-Language": "es-419,es;q=0.9:",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

response = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/1.0-_baths/?searchQueryState=%7B%22pagination"
                        "%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.37164497375488%2C%22east%22%3A-122"
                        ".17080116271973%2C%22south%22%3A37.75225820732334%2C%22north%22%3A37.86631630265098%7D%2C"
                        "%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max"
                        "%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min"
                        "%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C"
                        "%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22"
                        "%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B"
                        "%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22"
                        "%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%7D", headers=headers)


web = response.text
soup = BeautifulSoup(web, "lxml")


Price = soup.find_all("div", {"class": "list-card-price"})
addrs = soup.find_all("address", {"class": "list-card-addr"})
links = soup.find_all("a",{"list-card-link"})


Prices = []
for p in Price:
    Prices.append(p.getText())


addrs1 = []
for a in addrs:
    addrs1.append(a.getText())

string = "https://www.zillow.com"
links_list = ["n"]

for link in links:
    numbers = 1
    i_link = link.get("href")
    if i_link[0] == "/":
        c_link = string+i_link
        if c_link == links_list[-1]:
            pass
        else:
            links_list.append(c_link)

links_completed = links_list[1:]


response.close()

# ---------------------------------------------------------------------------------------------------------------------

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





for n in range(len(Prices)):
    googleurl = "https://docs.google.com/forms/d/e/1FAIpQLScpAwzdJFnVyJITaNdbk7WTyfqivgFzSH6mdUB0mF-3bsmz6g/viewform?usp=sf_link"

    google = driver.get(googleurl)

    propiedad = driver.find_element_by_css_selector("input[jsname = YPqjbf ")
    propiedad.send_keys(addrs1[n])
    time.sleep(3)

    precio1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    precio1.send_keys(Prices[n])

    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys((links_completed[n]))

    sumit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    sumit.click()
    time.sleep(2)







