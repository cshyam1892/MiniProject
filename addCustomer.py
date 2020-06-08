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

#add a customer
def customer():
    driver.find_element_by_xpath("//span[text()='Customers']").click()
    element = driver.find_element_by_link_text('Add new')
    element.click()
    element = driver.find_element_by_id("first_name")
    element.send_keys("Monk")
    element = driver.find_element_by_id("last_name")
    element.send_keys("Buddhist")
    element = driver.find_element_by_id("address")
    element.send_keys("Tibet")
    element = driver.find_element_by_id("phone")
    element.send_keys("0223266666")
    element = driver.find_element_by_id("email")
    element.send_keys("monk@gmail.com")
    driver.find_element_by_css_selector(".btn-danger").click()

login()
customer()
