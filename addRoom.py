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

#add a room
def aroom():
    driver.find_element_by_xpath("//span[text()='Rooms']").click()
    element = driver.find_element_by_link_text('Add new')
    element.click()
    element = driver.find_element_by_id("room_number")
    element.send_keys("102")
    element = driver.find_element_by_id("floor")
    element.send_keys("1")
    element = driver.find_element_by_id("description")
    element.send_keys("Single bed room with attach bathroom")
    driver.find_element_by_css_selector(".btn-danger").click()

login()
aroom()
