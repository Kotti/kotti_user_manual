#!/usr/bin/env python
import os
from selenium import webdriver

chrome_driver_path = "{0}/chromedriver".format(os.getcwd())

browser = webdriver.Chrome(chrome_driver_path)
browser.get('http://127.0.0.1:5000/')
browser.save_screenshot('main.png')
browser.quit()
