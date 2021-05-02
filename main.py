from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="path to chrome executable")

driver.maximize_window()
driver.get("https://kaushal1014.github.io/")
time.sleep(5)

text=["ass","idiot"]
for words in text:
    check=words 

try:
    x=driver.find_element_by_xpath(f"//*[contains(text(),'{check}')]")
    print("Bad word found")
except NoSuchElementException:
    print("No bad words found")
driver.close()

