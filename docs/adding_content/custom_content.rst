==============
Custom Content
==============

Kotti comes with built-in Document, Image, and File content types. These are
general purpose content types. Keeping Kotti simple, with a focus on solid
programming for these content types is an important part of the vision for the
software. 

Add-ons are smaller software components that augment the base Kotti system. Add
kotti_blog to your Kotti website and you get two new content types, Blog and
BlogEntry. Add kotti_media to your website and you get Video, Audio, and other
specialized content types.

Add-ons usually restrict how their content types can be added. For kotti_blog,
BlogEntry items are addable only to a Blog. For kotti_media, the M4aFile
content type is one of the available Audio media types. Kotti add-ons come with
their own documentation that describes the available content types and how they
work together.

Kotti maintains a system for add-ons called the Kollective, a listing and
collaborative work area where software developers produce and maintain add-ons.
Maintaining software can be a chore. The Kollective uses automation to run
tests on add-ons to assure compatibility with Kotti as fixes and advancements
are made.

Browse the Kollective for available add-ons, and ask your website administrator
to install the ones you need. It is good to settle on add-ons that are
needed, after an initial phase of experimentation, because once you start
adding content with a given add-on, the database contains entries encoded with
the specific structure of the add-on's content types.
