from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')

url = "http://localhost/MYSERVER/login.html"
driver.get(url)
driver.find_element_by_id("u_name").send_keys("abe")
driver.find_element_by_id("pwd").send_keys("1")

driver.implicitly_wait(5)#암묵적으로 기다리자.

driver.find_element_by_id("mysubmit").click()

url = "http://localhost/MYSERVER/secret"
driver.get(url)

print(driver.page_source)

all_options = driver.find_elements_by_tag_name("td")
for option in all_options:
    print(option.text)