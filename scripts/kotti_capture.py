#!/usr/bin/env python
import os
import time
import contextlib
import re
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

fruits = [u'Apple', u'Avocado', u'Banana']
allfruits = [u'Apple', u'Avocado', u'Banana', u'Cantaloupe', u'Cherry', u'Grape',
          u'Kiwi', u'Lemon', u'Nectarine', u'Orange', u'Peach', u'Pineapple',
          u'Plum', u'Strawberry']

TOOLBAR_HEIGHT = 40
MENU_HEIGHT = 40
BASE_URL = 'http://127.0.0.1:5000'

def log_in(browser):

    browser.get('http://127.0.0.1:5000/login')

    elem = browser.find_element_by_name("login")
    elem.send_keys("Admin")

    elem = browser.find_element_by_name("password")
    elem.send_keys("qwerty")

    browser.save_screenshot('../docs/images/logging_in.png')
    RPT('logging_in captured')

    elem = browser.find_element_by_name("submit")
    elem.click()

    _logged_in = True

    browser.save_screenshot('../docs/images/logged_in.png')
    RPT('logged_in captured')

    RPT('logged in')

    return browser

def log_out(browser):
    elem = browser.find_element_by_link_text('Administrator')
    elem.click()

    elem = browser.find_element_by_link_text('Logout')
    elem.click()

    _logged_in = False

    RPT('logged out')

def not_logged_in(browser):

    browser.get('http://127.0.0.1:5000')

    browser.save_screenshot('../docs/images/not_logged_in.png')

    elem_footer = browser.find_element_by_tag_name('footer')
    #elem_aliens = elem_footer.find_element_by_tag_name('p')

    crop_full_width_and_save(
            "../docs/images/not_logged_in.png",
            0,
            elem_footer.location['y'] + elem_footer.size['height'] + 30,
            "../docs/images/not_logged_in.png")

    RPT('not_logged_in captured')

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
    wait = WebDriverWait(browser, 10)

    elem = browser.find_element_by_link_text('Add')
    elem.click()

    elem = browser.find_element_by_link_text("Document")
    elem.click()

    elem_title = browser.find_element_by_name('title')
    elem_title.send_keys(title)

    if description:
        elem_description = browser.find_element_by_id('deformField2')
        elem_description.send_keys(description)

    if body:
        elem_iframe = browser.switch_to_frame('deformField4_ifr')
        # Firefox bug:
        # http://code.google.com/p/selenium/issues/detail?id=2355
        elem_body = wait.until(lambda br: br.find_element_by_id('tinymce'))
        elem_body.send_keys(body)

    browser.switch_to_default_content()

    elem_save = browser.find_element_by_id('deformsave')
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

# These functions produce the screen captures.

def toolbar_anonymous(browser):
    elem_brand = browser.find_element_by_class_name('brand')
    elem_search = browser.find_element_by_id('form-search')
    elem_navbar = browser.find_element_by_class_name('navbar-inner')
    elem_nav = elem_navbar.find_element_by_class_name('nav')
    browser.save_screenshot('../docs/images/anonymous.png')
    crop_bbox_of_elems_and_save('../docs/images/anonymous.png',
                                '../docs/images/toolbar_anonymous.png',
                                [elem_brand, elem_search, elem_nav],
                                (10, 10, 10, 10))
    RPT('toolbar_anonymous captured')

def editor_bar(browser):
    if click_main_nav_item(browser, 'Fruits'):
        browser.save_screenshot('../docs/images/fruits_view.png')
        elem_state_span = browser.find_element_by_class_name('state-private')
        elem_administrator = \
                browser.find_element_by_link_text('Administrator')
        crop_bbox_of_elems_and_save('../docs/images/fruits_view.png',
                                    '../docs/images/editor_bar.png',
                                    [elem_state_span, elem_administrator],
                                    (10, 10, 10, 10))
        RPT('editor_bar captured')

def state_menu(browser):
    capture_menu(browser, "state_menu", "Private", 4, 3)

def add_menu(browser):
    capture_menu(browser, "add_menu", "Add", 4, 3)

def actions_menu(browser):
    capture_menu(browser, "actions_menu", "Actions", 4, 3,
                 submenu_link_text='Set default view')

def admin_menu(browser):
    capture_menu(browser, "admin_menu", "Administrator", 4, 3)

def contents_action_buttons(browser):

    if click_main_nav_item(browser, 'Fruits'):

        elem = browser.find_element_by_link_text('Contents')
        elem.click()

        elem_copy = browser.find_element_by_name('copy')
        elem_hide = browser.find_element_by_name('hide')

        target_img = "../docs/images/contents_action_buttons.png"
        browser.save_screenshot(target_img)

        crop_bbox_of_elems_and_save(target_img,
                                    target_img,
                                    [elem_copy, elem_hide],
                                    (10, 10, 10, 10))

        RPT('contents_action_buttons captured')
    else:
        RPT('PROBLEM with contents_action_buttons capture')

def delete_about_document(browser):

    wait = WebDriverWait(browser, 10)

    if click_main_nav_item(browser, 'About'):
        save_screenshot_full(browser, 'default_about.png')

        elem_actions = \
                wait.until(lambda br: br.find_element_by_link_text('Actions'))
        elem_actions.click()

        save_screenshot_full(browser, 'default_about_actions_menu.png')

        elem_delete = \
                wait.until(lambda br: br.find_element_by_link_text('Delete'))
        elem_delete.click()

        elem_delete = \
                wait.until(lambda br: br.find_element_by_name('delete'))

        # There is no footer on the confirmation page.
        save_screenshot_full(browser,
                             'default_about_delete_confirmation.png',
                             elem_top=None,
                             elem_bottom=elem_delete)

        elem_delete.click()

        save_screenshot_full(browser, 'default_about_delete_flash_message.png')

# Hangs in Chrome without bug fix. With Firefox, can't even get this far,
# because of bug with adding text to tinymce body.
def edit_about_document(browser):

    # The goal of this edit is to make the phrase "the fruits" in the existing
    # body text into a link to the "Fruits" document.

    if click_main_nav_item(browser, 'About'):
        browser.get(BASE_URL + "/about/@@edit")

        # Bug fix (See below where hang occurs if this script is not run):
        # http://stackoverflow.com/questions/11846339/chrome-webdriver-hungs-when-currently-selected-frame-closed
        # (See link to bug there).
        browser.execute_script("""(function() {
var domVar;
if (window.tinymce && window.tinymce.DOM) {
    domVar = window.tinymce.DOM 
}
else if (window.tinyMCE && window.tinyMCE.DOM) {
    domVar = window.tinyMCE.DOM 
}
else {
    return;
}
var tempVar = domVar.setAttrib;console.log(123)
domVar.setAttrib = function(id, attr, val) {
    if (attr == 'src' && typeof(val)== 'string' &&(val + "").trim().match(/javascript\s*:\s*("\s*"|'\s*')/)) {
        console.log("Cool");
        return;
    }
    else {
        tempVar.apply(this, arguments);
    }
}

}());""")

        elem_deformField4 = browser.find_element_by_id('deformField4_tbl')
        elem_deformField4.click()

        elem_iframe = browser.switch_to_frame('deformField4_ifr')
        editor = browser.switch_to_active_element()
        editor.click()

        move_right_keys = [Keys.ARROW_LEFT for i in xrange(10)]
        move = ActionChains(browser).send_keys_to_element(
                editor, ''.join(move_right_keys))
        move.perform()

        shift_key_down = ActionChains(browser).key_down(Keys.SHIFT)
        shift_key_down.perform()

        selection = ActionChains(browser).send_keys_to_element(
                editor, ''.join(move_right_keys))
        selection.perform()

        # This SHIFT key_up doesn't take effect somehow, and another one
        # is needed later.
        shift_key_up = ActionChains(browser).key_up(Keys.SHIFT)
        shift_key_up.perform()

        browser.switch_to_default_content()

        wait = WebDriverWait(browser, 10)
    
        browser.find_element_by_css_selector("span.mceIcon.mce_link").click()

        def link_dialog_appeared(browser, wait):
            elem = wait.until(
                    lambda br: br.find_element_by_class_name('clearlooks2'))
            if elem:
                #elem.click()
                return True
            return False

        wait.until(lambda browser: link_dialog_appeared(browser, wait))

        tinymce_popup_frame = \
                browser.find_element_by_css_selector('iframe[id^="mce"]')

        browser.switch_to_frame(tinymce_popup_frame)

        elem_href = browser.switch_to_active_element()

        # For unknown reason, have to release SHIFT again.
        shift_key_up = ActionChains(browser).key_up(Keys.SHIFT)
        shift_key_up.perform()

        href_add = ActionChains(browser).send_keys_to_element(
                elem_href, '127.0.0.1:5000/fruits')
        href_add.perform()

        insert = browser.find_element_by_name("insert")
        insert.click()

        # Without the bug fix script above, the dialog comes down, but it hangs
        # here, with the new link looking swell in the editor.

        browser.switch_to_default_content()

        browser.find_element_by_id("deformsave").click()


#####################
# Utility Functions

def click_main_nav_item(browser, text):
    wait = WebDriverWait(browser, 10)
    browser.switch_to_default_content()
    elem_main_nav = wait.until(lambda br: br.find_element_by_link_text(text))
    if elem_main_nav:
        elem_main_nav.click()
        RPT(text + ' clicked')
        return True
    return False

def add_fruits_content(browser):

    add_document(browser, 'Fruits', '', '')

    for fruit in fruits:
        if click_main_nav_item(browser, 'Fruits'):
            image_name = "{0}_1200.jpg".format(fruit)
            fruit_path = os.getcwd() + "/fruit_images/{0}".format(image_name)
            add_image(browser, fruit, '', os.path.abspath(fruit_path))
        else:
            RPT('PROBLEM with adding content')

def save_screenshot_full(browser, image_name, elem_top=None, elem_bottom=None):

    if not elem_top:
        top = 0
    else:
        top = elem_top.location['y'] - 30

    if not elem_bottom:
        bottom = 0
    else:
        bottom = elem_bottom.location['y'] + elem_bottom.size['height'] + 30

    wait = WebDriverWait(browser, 10)

    image_path = "../docs/images/{0}".format(image_name)

    browser.save_screenshot(image_path)

    crop_full_width_and_save(image_path, top, bottom, image_path)

    RPT("{0} captured".format(image_name))

def crop_full_width_and_save(source_img, top, bottom, target_img):
    im = Image.open(source_img)
    width, height = im.size
    if not top:
        top = 0
    if not bottom:
        bottom = height
    im = im.crop((0, top, width, bottom))
    im.save(target_img)

def crop_bbox_of_elems_and_save(source_img, target_img, elems, margins):

    xmin = min([elem.location['x'] for elem in elems])
    xmax = max([elem.location['x'] + elem.size['width'] for elem in elems])

    ymin = min([elem.location['y'] for elem in elems])
    ymax = max([elem.location['y'] + elem.size['height'] for elem in elems])

    left_margin, right_margin, top_margin, bottom_margin = margins

    im = Image.open(source_img)

    im_width, im_height = im.size

    left = xmin - left_margin
    right = xmax + right_margin
    top = ymin - top_margin
    bottom = ymax + bottom_margin

    if left < 0:
        left = xmin
    if right > im_width:
        right = im_width
    if top < 0:
        top = ymin
    if bottom > im_height:
        bottom = im_height

    area = im.crop((left, top, right, bottom))

    area.save(target_img)

################
# Main routine

doc_files = ['../docs/introduction/overview.rst',
             '../docs/introduction/users_and_roles.rst',
             '../docs/adding_content/documents.rst',
             '../docs/editing_content/contents_view.rst',
             '../docs/editing_content/view_selection.rst']

chrome_driver_path = "{0}/chromedriver".format(os.getcwd())

# This will capture: logging_in
#                    logged_in
browser = log_in(webdriver.Chrome(chrome_driver_path))
#browser = log_in(webdriver.Firefox())

# Set the browser to full size to avoid wrapping issues.
browser.maximize_window()

# We have to pay attention to the order of ops somewhat, being careful about
# adding content before making screen captures that expect certain content to
# be there.

# This will capture: logging_in
delete_about_document(browser)

add_document(browser, "About",
             "This website is for our fruit stand.",
             "We have many fruits available. Choose the fruit you want.")

browser.find_element_by_class_name('brand').click()

# Now that we are logged in,
add_fruits_content(browser)

# Capture editor_bar:
editor_bar(browser)

edit_about_document(browser)

# Scan docs for needed screen captures, coming in the form of image entries in
# the Sphinx docs. The image names should match names of functions explicitly
# called here.
#for doc_file in doc_files:
#    for line in open(doc_file):
#        if line.startswith('.. Image::'):
#            image_name = line[10:].strip()
#            if image_name not in ['logged_in', 'toolbar_anonymous',
#                                  'editor_bar', 'not_logged_in']:
#                func_name = image_name[len('../images/'):-4]
#                if func_name in globals():
#                    globals()[func_name](browser)
#                else:
#                    print 'Function', func_name, 'NOT FOUND.'

log_out(browser)

# Capture after we have logged out.
not_logged_in(browser)

# Capture a plain toolbar.
toolbar_anonymous(browser)


browser.quit()
