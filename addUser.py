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

def user():
    driver.find_element_by_xpath("//span[text()='User management']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//span[contains(.,'Users')]").click()
    driver.find_element_by_link_text('Add new').click()
    driver.find_element_by_id("name").send_keys("new user")
    driver.find_element_by_id("email").send_keys("newuser@gmail.com")
    driver.find_element_by_id("password").send_keys("12345")
    driver.find_element_by_id("select2-role_id-container").click()
    ele.click()
    #element = driver.find_element_by_css_selector(".select2-search__field")
    #element.send_keys("Simple user")
    element = driver.find_element_by_css_selector(".btn-danger")
    element.click()


login()
user()
