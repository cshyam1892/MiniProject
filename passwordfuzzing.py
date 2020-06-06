#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

start = time.time()

#set up driver
driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8000")

def login():
    element = driver.find_element_by_name("email")
    element.send_keys("test@test.com")
    element = driver.find_element_by_name("password")
    element.send_keys("password")
    driver.find_element_by_xpath('//button[@type="submit"]').click()


#change password
def cpassword():
    driver.find_element_by_xpath("//span[text()='Change password']").click()
    element = driver.find_element_by_id("current_password")
    element.send_keys("password1")
    element = driver.find_element_by_id("new_password")
    element.send_keys("password")
    element = driver.find_element_by_id("new_password_confirmation")
    element.send_keys("password")
    driver.find_element_by_css_selector(".btn-danger").click()
    time.sleep(5)

login()
