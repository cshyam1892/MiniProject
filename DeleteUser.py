#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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

def deleteAdmin():
    driver.find_element_by_xpath("//span[text()='User management']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[contains(.,'Users')]").click()
    element = driver.find_element_by_xpath("//tr[2]/td")
    element.click()
    ele = driver.find_element_by_link_text('Delete selected')
    ele.click()
                                       

login()
deleteAdmin()
