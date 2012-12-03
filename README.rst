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

Run Kotti::

  pserve app.ini

In a second terminal
--------------------

For using Chrome, see the list of drivers at
http://code.google.com/p/chromedriver/downloads/list, then download the
chromedriver to the scripts directory.

Look at capture_main.py in the scripts/ directory::

  #!/usr/bin/env python
  import os
  from selenium import webdriver

  chrome_driver_path = "{0}/chromedriver".format(os.getcwd())

  browser = webdriver.Chrome(chrome_driver_path)
  browser.get('http://127.0.0.1:5000/')
  browser.save_screenshot('main.png')
  browser.quit()

Then run the script::

  python capture_main.py

You should then have a main.png file in the scripts/ directory, along with a
chromedriver.log.
