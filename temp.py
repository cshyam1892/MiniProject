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

#find rooms
def froom():
    driver.find_element_by_xpath("//span[text()='Find room']").click()
    #driver.find_element_by_id("time_from").click()
    driver.find_element_by_xpath("//input[@name='time_from']").clear() 
    driver.find_element_by_xpath("//input[@name='time_from']").send_keys("2020-06-05 02:42")
    #driver.find_element_by_id("time_from").click()
    #driver.find_element_by_id("time_to").click()
    #element = driver.find_element_by_css_selector(".btn-danger")
    #element.click()

login()
froom()
