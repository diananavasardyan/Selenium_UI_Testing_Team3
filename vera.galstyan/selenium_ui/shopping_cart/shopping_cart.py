#This test case created by Vera Galstyan

#!usr\bin\env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
browser = webdriver.Chrome(executable_path = r"C:\Users\Admin\Desktop\Webdriver\chromedriver.exe", options = chrome_options)
browser.get("https://www.saucedemo.com/")
username_form = username_form = browser.find_element_by_id("user-name")
login = browser.find_element_by_xpath('//*[@id="login_credentials"]').text.split()[5]
username_form.send_keys(login)
password_form = browser.find_element_by_id("password")
password = browser.find_element_by_xpath('//*[@class="login_password"]').text.split()[4]
password_form.send_keys(password)
login_button = browser.find_element_by_id("login-button").click()
actual = browser.find_element_by_id("add-to-cart-sauce-labs-backpack").send_keys("ADD TO CART")
expect = "https://www.saucedemo.com/inventory.html"

if  actual == expect:
    print("Test case is passed.")
else:
    print("Test case is failed.")