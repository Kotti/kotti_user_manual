#!/usr/bin/env python
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image

TOOLBAR_HEIGHT = 40
MENU_HEIGHT = 40

doc_files = ['../docs/kotti_basics/overview.rst',
             '../docs/kotti_basics/users_and_roles.rst',
             '../docs/adding_content/documents.rst',
             '../docs/editing_content/view_selection.rst']

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

def capture_menu(browser, image_name, link_text,
                 margin_division_factor, menu_height_factor,
                 submenu_link_text=None):
    elem = browser.find_element_by_link_text(link_text)
    elem.click()

    left, top = (elem.location['x'], elem.location['y'])
    menu_width, menu_height = (elem.size['width'], elem.size['height'])
    left -= menu_width / margin_division_factor
    top -= menu_height / margin_division_factor

    elem = browser.find_element_by_class_name("dropdown-menu")
    dropdown_menu_width, dropdown_menu_height = \
            (elem.size['width'], elem.size['height'])

    if submenu_link_text:

        elem = browser.find_element_by_link_text(submenu_link_text)
        hov = ActionChains(browser).move_to_element(elem)
        hov.perform()

        image_path = "../docs/images/{0}.png".format(image_name)
        browser.save_screenshot(image_path)

        im = Image.open(image_path)

        submenu_width, submenu_height = (elem.size['width'],
                                         elem.size['height'])

        width, height = \
                (dropdown_menu_width + submenu_width,
                 menu_height + \
                         menu_height_factor * dropdown_menu_height + \
                         menu_height_factor * submenu_height)

    else:
        image_path = "../docs/images/{0}.png".format(image_name)
        browser.save_screenshot(image_path)

        im = Image.open(image_path)

        width, height = \
                (dropdown_menu_width,
                 menu_height + menu_height_factor * elem.size['height'])

    im = im.crop((left,
                  top,
                  left + width + width/margin_division_factor,
                  top + height + height/margin_division_factor))

    im.save(image_path)

def actions_menu(browser):
    capture_menu(browser, "actions_menu", "Actions", 4, 3,
                 submenu_link_text='Set default view')

def add_menu(browser):
    capture_menu(browser, "add_menu", "Add", 4, 3)

browser = log_in(browser)

for doc_file in doc_files:
    for line in open(doc_file):
        if line.startswith('.. Image::'):
            image_name = line[10:].strip()
            globals()[image_name[len('../images/'):-4]](browser)

browser.quit()
