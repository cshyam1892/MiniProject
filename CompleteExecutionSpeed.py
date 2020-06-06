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


#find rooms
def froom():
    driver.find_element_by_xpath("//span[text()='Find room']").click()
    driver.find_element_by_id("time_from").click()
    driver.find_element_by_id("time_to").click()
    element = driver.find_element_by_css_selector(".btn-danger")
    element.click()

#change password
#def cpassword():
    #driver.find_element_by_xpath("//span[text()='Change password']").click()
    #element = driver.find_element_by_id("current_password")
    #element.send_keys("password1")
    #element = driver.find_element_by_id("new_password")
    #element.send_keys("password")
    #element = driver.find_element_by_id("new_password_confirmation")
    #element.send_keys("password")
    #driver.find_element_by_css_selector(".btn-danger").click()
    #time.sleep(5)


def logout():
    driver.find_element_by_xpath("//a[contains(@onclick,'submit')]").click()

#driver.execute_script('''window.open("https://www.bunningscareers.com.au/search?search=cvid-JKGXO","_blank");''')
end = time.time()
print("application took", end - start) 

login()
customer()
aroom()
booking()
froom()
#cpassword()
logout()
