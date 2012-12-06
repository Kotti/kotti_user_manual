#!/usr/bin/env python
import os
import time
import contextlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image

# RPT = report to console
reporting = True
timing = True

start = time.time()

def RPT(message):
    if reporting:
        if timing:
            print "{0} -- {1:g} seconds".format(message, time.time() - start)
        else:
            print message

fruits = [u'Apple', u'Avocado', u'Banana', u'Cantaloupe', u'Cherry', u'Grape',
          u'Kiwi', u'Lemon', u'Nectarine', u'Orange', u'Peach', u'Pineapple',
          u'Plum', u'Strawberry']

TOOLBAR_HEIGHT = 40
MENU_HEIGHT = 40

def log_in(browser):

    browser.get('http://127.0.0.1:5000/login')

    elem = browser.find_element_by_name("login")
    elem.send_keys("Admin")

    elem = browser.find_element_by_name("password")
    elem.send_keys("qwerty")

    elem = browser.find_element_by_name("submit")
    elem.click()

    _logged_in = True

    RPT('logged in')

    return browser

def log_out(browser):
    elem = browser.find_element_by_link_text('Administrator')
    elem.click()

    elem = browser.find_element_by_link_text('Logout')
    elem.click()

    _logged_in = False

    RPT('logged out')

def logged_in(browser):

    browser.save_screenshot('../docs/images/logged_in.png')

    RPT('logged_in captured')

def not_logged_in(browser):

    browser.get('http://127.0.0.1:5000')

    browser.save_screenshot('../docs/images/not_logged_in.png')

    RPT('not_logged_in captured')

def main_menu(browser):

    logged_in(browser)

    im = Image.open("../docs/images/logged_in.png")
    width, height = im.size
    box = (0, int(TOOLBAR_HEIGHT),
           int(width), int(TOOLBAR_HEIGHT + MENU_HEIGHT))
    im = im.crop(box)
    im.save("../docs/images/main_menu.png")

    RPT('main_menu captured')

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
        hover = ActionChains(browser).move_to_element(elem)
        hover.perform()

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

    box = (int(left), int(top),
           int(left + width + width/margin_division_factor),
           int(top + height + height/margin_division_factor))

    im = im.crop(box)

    im.save(image_path)

    RPT("{0} captured".format(image_path.split('/')[-1]))

def add_document(browser, title, description, body):
    elem = browser.find_element_by_link_text('Add')
    elem.click()

    elem = browser.find_element_by_link_text("Document")
    elem.click()

    elem_title = browser.find_element_by_name('title')
    elem_title.send_keys(title)

    if description:
        elem_description = browser.find_element_by_name('description')
        elem_description.send_keys(description)

    if body:
        elem_body = browser.find_element_by_id('tinymce')

        elem_p = elem_body.find_element_by_tag_name('p')
        elem_p.send_keys(body)

    wait = WebDriverWait(browser, 10)
    elem_save = browser.find_element_by_name('save')
    elem_save.click()

    def save_was_successful(browser, wait):
        elem = wait.until(lambda br: br.find_element_by_id('messages'))
        for child in elem.find_elements_by_xpath('./*'):
            if 'Success' in child.text:
                return True
        return False

    wait.until(lambda browser: save_was_successful(browser, wait))

    RPT('document {0} added'.format(title))

def add_image(browser, title, description, image_abspath):

    elem = browser.find_element_by_link_text('Add')
    elem.click()

    elem = browser.find_element_by_link_text("Image")
    elem.click()

    elem_title = browser.find_element_by_name('title')
    elem_title.send_keys(title)

    if description:
        elem_description = browser.find_element_by_name('description')
        elem_description.send_keys(description)

    elem = browser.find_element_by_name("upload")
    elem.send_keys(image_abspath)

    wait = WebDriverWait(browser, 10)
    elem_save = browser.find_element_by_name('save')
    elem_save.click()

    def upload_was_successful(browser, wait):
        elem = wait.until(lambda br: br.find_element_by_id('messages'))
        for child in elem.find_elements_by_xpath('./*'):
            if 'Success' in child.text:
                return True
        return False

    wait.until(lambda browser: upload_was_successful(browser, wait))

    RPT('image {0} added'.format(title))

###################
# Specific Images

# These match functions which produce the images.

def actions_menu(browser):
    capture_menu(browser, "actions_menu", "Actions", 4, 3,
                 submenu_link_text='Set default view')

def add_menu(browser):
    capture_menu(browser, "add_menu", "Add", 4, 3)

def admin_menu(browser):
    capture_menu(browser, "admin_menu", "Administrator", 4, 3)

def contents_action_buttons(browser):

    if click_main_nav_item(browser, 'Fruits'):

        elem = browser.find_element_by_link_text('Contents')
        elem.click()

        browser.save_screenshot("../docs/images/contents_action_buttons.png")

        RPT('contents_action_buttons captured')
    else:
        RPT('PROBLEM with contents_action_buttons capture')



#####################
# Utility Functions

def click_main_nav_item(browser, text):
    # First put the context on the root.
    elem_brand = browser.find_element_by_class_name('brand')
    elem_brand_link = elem_brand.find_element_by_tag_name('a')
    elem_brand_link.click()

    # Now find the top-level nav item and click it, if found.
    elem_navbar = browser.find_element_by_class_name('navbar-inner')
    elem_nav = elem_navbar.find_element_by_class_name('nav')
    for li in elem_nav.find_elements_by_tag_name('li'):
        for a in li.find_elements_by_tag_name('a'):
            if text in a.text:
               a.click()
               RPT(text + ' clicked')
               return True

    return False

def add_content(browser):

    add_document(browser, 'Fruits', '', '')

    for fruit in fruits:
        if click_main_nav_item(browser, 'Fruits'):
            image_name = "{0}_1200.jpg".format(fruit)
            fruit_path = os.getcwd() + "/fruit_images/{0}".format(image_name)
            add_image(browser, fruit, '', os.path.abspath(fruit_path))
        else:
            RPT('PROBLEM with contents_action_buttons capture')

################
# Main routine

doc_files = ['../docs/kotti_basics/overview.rst',
             '../docs/kotti_basics/users_and_roles.rst',
             '../docs/adding_content/documents.rst',
             '../docs/editing_content/contents_view.rst',
             '../docs/editing_content/view_selection.rst']

chrome_driver_path = "{0}/chromedriver".format(os.getcwd())

browser = log_in(webdriver.Chrome(chrome_driver_path))

# Set the browser to full size to avoid wrapping issues.
browser.maximize_window()

# We have to pay attention to the order of ops somewhat, being careful about
# the logging in / logging out main checks, but also about adding content
# before making screen captures that expect the content to be there. This is
# done by checking global flags.

# This will log in, then capture general logged_in image.
logged_in(browser)

# Now that we are logged in,
add_content(browser)

# Now service requests for screen captures, coming in the form of image entries
# in the Sphinx docs.
for doc_file in doc_files:
    for line in open(doc_file):
        if line.startswith('.. Image::'):
            image_name = line[10:].strip()
            if image_name not in ['logged_in', 'not_logged_in']:
                globals()[image_name[len('../images/'):-4]](browser)

# These steps will log out, then capture not_logged_in image.
log_out(browser)
not_logged_in(browser)

browser.quit()
