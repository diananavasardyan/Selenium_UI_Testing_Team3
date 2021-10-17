#This test case created by Vera Galstyan

#!usr\bin\env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
browser = webdriver.Chrome(executable_path = r"C:\Users\Admin\Desktop\Webdriver\chromedriver.exe", options = chrome_options)
browser.get("https://www.saucedemo.com/")
browser.find_element_by_id("user-name").send_keys("standard_user")
browser.find_element_by_id("password").send_keys("secret_sauce")
browser.find_element_by_id("login-button").click()
actual = browser.find_element_by_id("add-to-cart-sauce-labs-backpack").send_keys("ADD TO CART")
browser.find_element_by_class_name( "shopping_cart_badge").click()
browser.find_element_by_id("checkout" ).click()

browser.find_element_by_id("first-name").send_keys("Vera")
browser.find_element_by_id("last-name").send_keys("Galstyan")
browser.find_element_by_id("postal-code").send_keys("111")
browser.find_element_by_id("continue").click()
browser.find_element_by_id("finish").click()
expect = "https://www.saucedemo.com/inventory.html"
if  actual == expect:
    print("Test case is passed.")
else:
    print("Test case is failed.")
