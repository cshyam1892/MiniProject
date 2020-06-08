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
    element.send_keys("123456")
    driver.find_element_by_xpath('//button[@type="submit"]').click()

#change password
def cpassword():
    driver.find_element_by_xpath("//span[text()='Change password']").click()
    element = driver.find_element_by_id("current_password")
    element.send_keys("123456")
    element = driver.find_element_by_id("new_password")
    element.send_keys("1234567")
    element = driver.find_element_by_id("new_password_confirmation")
    element.send_keys("1234567")
    driver.find_element_by_css_selector(".btn-danger").click()
    time.sleep(5)

def logout():
    driver.find_element_by_xpath("//a[contains(@onclick,'submit')]").click()


login()
cpassword()
logout()

