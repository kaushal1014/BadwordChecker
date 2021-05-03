from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

url=input("Enter url:")

good_list=["giraffe"," elephant"," onion", "peanut butter", "myexample 123"]
bad_list=["The Committee shall monitor and review technological and legislative changes affecting intellectual property policy and shall report to relevant faculty and administrative bodies, when such changes affect existing policies.","The committee shall serve as a forum for the receipt and discussion of proposals to change existing institutional policy and/or to provide recommendations for contract negotiations"]
for good in good_list:
    good_words=good

for bad in bad_list:
    bad_words=bad

driver = webdriver.Chrome(executable_path="C:\\pythonProjects\\WordChecker - Copy\\chromedriver.exe")

driver.maximize_window()
driver.get(url)
time.sleep(5)


body=driver.find_element_by_css_selector("body")
time.sleep(5)
content=(body.text)
if any(good_words in content for good_words in good_list):
    print("good words found")
    
else:
    print("No good words found")
if any(bad_words in content for bad_words in bad_list):
    print("bad words found")
else:
    print("No bad words found")
driver.close()

