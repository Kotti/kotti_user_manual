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

def capture_menu(browser, image_name, link_text, menu_class_name):
    elem = browser.find_element_by_link_text(link_text)
    elem.click()

    left, top = (elem.location['x'], elem.location['y'])
    menu_width, menu_height = (elem.size['width'], elem.size['height'])
    left -= menu_width / 4
    top -= menu_height / 4

    image_path = "../docs/images/{0}.png".format(image_name)
    browser.save_screenshot(image_path)

    elem = browser.find_element_by_class_name(menu_class_name)

    im = Image.open(image_path)
    width, height = (elem.size['width'],
                     menu_height + 3 * elem.size['height'])
    im = im.crop((left, top, left + width + width/4, top + height + height/4))
    im.save(image_path)

def actions_menu(browser):
    capture_menu(browser, "actions_menu", "Actions", "actions-menu")

def add_menu(browser):
    capture_menu(browser, "add_menu", "Add", "dropdown-menu")

browser = log_in(browser)

for doc_file in doc_files:
    for line in open(doc_file):
        if line.startswith('.. Image::'):
            image_name = line[10:].strip()
            globals()[image_name[len('../images/'):-4]](browser)

browser.quit()
