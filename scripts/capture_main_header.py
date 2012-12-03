#!/usr/bin/env python
import os
from selenium import webdriver
from PIL import Image

chrome_driver_path = "{0}/chromedriver".format(os.getcwd())

browser = webdriver.Chrome(chrome_driver_path)
browser.get('http://127.0.0.1:5000/')
browser.save_screenshot('main.png')
browser.quit()

im = Image.open("main.png")
width, height = im.size
im = im.crop((0,0,width,100))
im.save("main_header.png")
