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

  pip install BlockDiag

PIL is already installed by Kotti requirements, and BlockDiag needs it. Check
that you have freetype2 on your system and that the installation of PIL sees
it.

Visit http://dejavu-fonts.org/wiki/Download and download into the /scripts
directory a set of fonts to use. We should probably try to use a given set.
So far, the set used is::

  wget http://sourceforge.net/projects/dejavu/files/dejavu/2.33/dejavu-fonts-ttf-2.33.tar.bz2 

After exploding the fonts, you should have the ttf files in::

  scripts/dejavu-fonts-ttf-2.33/ttf/

Run Kotti from the kotti_user_manual virtualenv directory::

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

Then run the script from the kotti_user_manual/scripts/ directory::

  python kotti_capture.py

This script saves screen capture images made with Selenium in the docs/images/
directory, and stores a chromedriver.log locally.

Then run the script::

  python kotti_blockdiag.py

This script uses the BlockDiag python package to generate PNG images for use in
the docs. It is possible to embed the BlockDiag diagram definitions in the rst
docs as directives. However, so far at least, to take advantage of ttf fonts as
this script does, we need to generate the PNG files on our own machines that
have PIL installed with freetype2 installed.

Working with the kotti_capture.py Script
----------------------------------------

In docs/ .rst files, add images as you normally would for Sphinx, according to
its documentation. The entries will have the form::

  ``.. Image:: ../images/add_menu.png``
  
You need to add a matching function, e.g. add_menu(), which must be made
through study of existing functions and experimentation. It is very much a
system where success is found by trial and error, combining attempts in the
Python code to use Selenium to find elements and do the screen captures with
element inspection using Browser tools to find ids, class names, and other
targets for Selenium.

Write functions that are dedicated to producing a given image, using whatever
steps are needed in python-selenium operations. It can be necessary to perform
several find, text and key entry, and click operations to achieve the desired
state before capturing the image. See existing functions for the pattern,
paying attention to the order of steps. Little things matter.

Working with the kotti_blockdiag.py Script
------------------------------------------

Add image directives for diagrams in the same way as you would for screen
captures, e.g. a diagram PNG image might be::

  ``.. Image:: ../images/anonymous_vs_authenticated.png``

Add a corresponding BlockDiag diagram definition in scripts/blockdiag, e.g.

  scripts/blockdiag/anonymous_vs_authenticated.diag

See existing examples and the BlockDiag docs, and experiment. 

Overall Routine
---------------

* Change / Run kotti_capture.py when something about Kotti changes, and fresh
  screen captures are needed, or when something is added or removed.
* Likewise, run kotti_blockdiag.py as needed when existing diagrams are
  modified or new ones added.
* Update docs files as needed for image directives from either kotti_capture.py
  or kotti_blockdiag.py.
* Update text of docs as needed.
* Rerun docs/make html.
* Push to github.com/Kotti/kotti_user_manual.
* Log in to readthedocs.org and manually click the Build button.
