from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="path to chrome executable")

driver.maximize_window()
driver.get("https://www.example.com")
time.sleep(5)

text=["the","words","you","want","to","find"]
for words in text:
    check=words 


body=driver.find_element_by_css_selector("body")
time.sleep(5)
content=(body.text)
if any(check in content for check in text):
    print("words found")
else:
    print("No words found")
driver.close()

