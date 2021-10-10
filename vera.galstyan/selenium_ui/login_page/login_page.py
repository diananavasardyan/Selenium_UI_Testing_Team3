#This test case was created by Vera Galstyan

#!/usr/bin/env python 3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome("executable_path https://www.saucedemo.com/inventory.html")
chrome_driver.get("https://www.saucedemo.com/inventory.html")
chrome_driver.find_element(By.ID("user-name" )).click()
chrome_driver.find_element(By.ID("password" )).click()
chrome_driver.find_element(By.ID("login-button" )).click()