from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

url=input("Enter url:")
if "https://www." not in url:
    https=url
else:
    https="https://www."+url

good=input("Enter the good words:")
bad=input("Enter the bad words:")
good_trimed=good.rstrip()
bad_trimed=bad.rstrip()
good_list = list(good_trimed.split(" ")) 
bad_list = list(bad_trimed.split(" ")) 
print(good_list)
print(bad_list)

for good in good_list:
    good_words=good

for bad in bad_list:
    bad_words=bad

driver = webdriver.Chrome(executable_path="C:\\pythonProjects\\WordChecker - Copy\\chromedriver.exe")

driver.maximize_window()
driver.get(https)
time.sleep(5)


body=driver.find_element_by_css_selector("body")
time.sleep(5)
content=(body.text)
if any(good_words in content for good_words in good_list):
    print(f"good words found")
    
else:
    print("No good words found")
if any(bad_words in content for bad_words in bad_list):
    print("bad words found")
else:
    print("No bad words found")
driver.close()

