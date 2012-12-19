kotti_user_manual
=================

A User Manual for Administrators and Users of Kotti CMS websites

Setup
=====

Make a virtualenv and prepare to use Kotti and selenium::
 
  mkvirtualenv kotti_user_manual
  wget https://raw.github.com/Pylons/Kotti/master/requirements.txt
  wget https://raw.github.com/Pylons/Kotti/master/app.ini
  pip install -U selenium
  pip install -r requirements.txt

  pip install Kotti

  pip install kotti_docs_theme

Run Kotti::

  pserve app.ini

In a Second Terminal
--------------------

Download the Selenium Java server and run it. On Mac OS X, after downloading
and clicking the tarball, it will explode and run. Or run with java yourself,
with, for example:

java -jar selenium-server-standalone-2.28.0.jar

In a Third Terminal
-------------------

For using Chrome, see the list of drivers at
http://code.google.com/p/chromedriver/downloads/list, then download the
chromedriver to the scripts directory. You do not have to download a
driver for using the Firefox webdriver.

Then run the script::

  python kotti_capture.py

This script saves images in the scripts/ directory, and stores a
chromedriver.log locally.

Using the Script
----------------

In docs/ .rst files, add images as you normally would, according to Sphinx
documentation. The entries will have the form ``.. Image::
../images/add_menu.png``. The script reads the docs files, looking for such
image entries, then calls the matching function, as with ``add_menu()``. 

Write functions that are dedicated to producing a given image, using whatever
steps are needed in python-selenium operations. It can be necessary to perform
several find, text and key entry, and click operations to achieve the desired
state before capturing the image. See existing functions for the pattern,
paying attention to the passing and order of creation for the browser object.
