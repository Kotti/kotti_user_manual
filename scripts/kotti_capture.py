#!/usr/bin/env python
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image

TOOLBAR_HEIGHT = 40
MENU_HEIGHT = 40

doc_files = ['../docs/kotti_basics/overview.rst',
             '../docs/kotti_basics/users_and_roles.rst',
             '../docs/adding_content/documents.rst']

chrome_driver_path = "{0}/chromedriver".format(os.getcwd())

browser = webdriver.Chrome(chrome_driver_path)

def not_logged_in(browser):

    browser.get('http://127.0.0.1:5000')

    browser.save_screenshot('../docs/images/not_logged_in.png')

def log_in(browser):

    browser.get('http://127.0.0.1:5000/login')

    elem = browser.find_element_by_name("login")
    elem.send_keys("Admin")

    elem = browser.find_element_by_name("password")
    elem.send_keys("qwerty")

    elem = browser.find_element_by_name("submit")
    elem.click()

    return browser

def logged_in(browser):

    browser.save_screenshot('../docs/images/logged_in.png')

def main_menu(browser):

    logged_in(browser)

    im = Image.open("../docs/images/logged_in.png")
    width, height = im.size
    im = im.crop((0, TOOLBAR_HEIGHT, width, TOOLBAR_HEIGHT + MENU_HEIGHT))
    im.save("../docs/images/main_menu.png")

def add_menu(browser):
    elem = browser.find_element_by_link_text("Add")
    elem.click()

    left, top = (elem.location['x'], elem.location['y'])
    add_width, add_height = (elem.size['width'], elem.size['height'])
    left -= add_width / 4
    top -= add_height / 4

    browser.save_screenshot('../docs/images/add_menu.png')

    elem = browser.find_element_by_class_name("dropdown-menu")

    im = Image.open("../docs/images/add_menu.png")
    width, height = (elem.size['width'], add_height + 3 * elem.size['height'])
    im = im.crop((left, top, left + width + width/4, top + height + height/4))
    im.save("../docs/images/add_menu.png")

browser = log_in(browser)

for doc_file in doc_files:
    for line in open(doc_file):
        if line.startswith('.. Image::'):
            image_name = line[10:].strip()
            globals()[image_name[len('../images/'):-4]](browser)

browser.quit()
