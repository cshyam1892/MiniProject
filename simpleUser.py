#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#set up driver
driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8000")

def login():
    element = driver.find_element_by_name("email")
    element.send_keys("simple@test.com")
    element = driver.find_element_by_name("password")
    element.send_keys("12345")
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(3)

def logout():
    driver.find_element_by_xpath("//a[contains(@onclick,'submit')]").click()

login()
logout()
