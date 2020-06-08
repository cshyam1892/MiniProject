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

#watch for bookings
def booking():
    driver.find_element_by_xpath("//span[text()='Bookings']").click()
    element = driver.find_element_by_link_text('Add new')
    element.click()
    driver.find_element_by_id("select2-customer_id-container").click()
    element = driver.find_element_by_css_selector(".select2-search__field")
    element.click()
    driver.find_element_by_id("select2-customer_id-results").click()
    element = driver.find_element_by_id("select2-room_id-container")
    element.click()
    driver.find_element_by_id("select2-room_id-results").click()
    driver.find_element_by_id("time_from").click()
    driver.find_element_by_id("time_to").click()
    element = driver.find_element_by_id("additional_information")
    element.click()
    element.send_keys("Booked with advance deposit")
    element = driver.find_element_by_xpath("//input[@name='amount']")
    element.send_keys("1200")
    element = driver.find_element_by_css_selector(".btn-danger")
    element.click()
    #driver.find_element_by_id("select2-customer_id-result-vek4-2").click()
    #driver.find_element_by_id("select2-room_id-container").click()
    #element = driver.find_element_by_css_selector(".select2-search__field")
    #element.send_keys("102")

login()
booking()
