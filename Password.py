#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

#sys.stdin = open('input.txt', 'r')
#for line in sys.stdin:
    #value = line.strip()

#set up driver
driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8000")

def login():
    element = driver.find_element_by_name("email")
    element.send_keys("test@test.it")
    element = driver.find_element_by_name("password")
    element.send_keys("aaaaaaaaaaaa")
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(3)

#loggin in with correct credentials
def login1():
    driver.find_element_by_name("email").clear()
    element = driver.find_element_by_name("email")
    element.send_keys("test@test.com")
    element = driver.find_element_by_name("password")
    element.send_keys("")
    driver.find_element_by_xpath('//button[@type="submit"]').click()

#change password
def cpassword():
    driver.find_element_by_xpath("//span[text()='Change password']").click()
    element = driver.find_element_by_id("current_password")
    element.send_keys(value)
    element = driver.find_element_by_id("new_password")
    element.send_keys(value)
    element = driver.find_element_by_id("new_password_confirmation")
    element.send_keys(value)
    driver.find_element_by_css_selector(".btn-danger").click()
    time.sleep(5)

def logout():
    driver.find_element_by_xpath("//a[contains(@onclick,'submit')]").click()

login()
login1()
cpassword()
logout()

