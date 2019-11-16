import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import sys

user1= ""
user2= ""

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")


elem_search_word = driver.find_element_by_class_name("_2hvTZ")
elem_search_word.send_keys(user1)

password = driver.find_element_by_name('password')
password.send_keys("")


driver.find_element_by_css_selector(".Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()

driver.implicitly_wait(10)
driver.find_element_by_css_selector(".aOOlW.HoLwm").click()


count = 0
flag = 1
while (flag == 1):
    try:
        print ('The count is:', count)
        myDynamicElement = driver.find_element_by_class_name("glyphsSpriteHeart__outline__24__grey_9")
        myDynamicElement.click()
        count = count + 1
    except Exception as e:
        print("You alredy LIKES " + str(e))
        flag = 0

print ("Done!")
driver.close()


driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")

elem_search_word = driver.find_element_by_class_name("_2hvTZ")
elem_search_word.send_keys(user2)

password = driver.find_element_by_name('password')
password.send_keys("")


driver.find_element_by_css_selector(".Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()

driver.implicitly_wait(10)
driver.find_element_by_css_selector(".aOOlW.HoLwm").click()


count = 0
flag = 1
while (flag == 1):
    try:
        print ('The count is:', count)
        myDynamicElement = driver.find_element_by_class_name("glyphsSpriteHeart__outline__24__grey_9")
        myDynamicElement.click()
        count = count + 1
    except Exception as e:
        print("You alredy LIKES " + str(e))
        flag = 0

print ("Done!")
driver.close()