Adding Custom Content
=====================

Kotti comes with built-in Document, Image, and File content types. These are
general purpose content types. Keeping Kotti simple, with a focus on solid
programming for these content types, is an important part of the vision for the
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

Kotti maintains a listing of add-ons on its website and has a collaborative
work area where software developers produce and maintain add-ons.  Maintaining
software can be a chore. Automation helps with this.  Tests are run on add-ons
to assure compatibility with Kotti as fixes and advancements are made.

Browse the list for available add-ons, and ask your website administrator to
install the ones you need. It is good to decide on add-ons that are really
needed for your website, after an initial phase of experimentation, because
once you start adding content in earnest, the database grows with entries
encoded with the specific structure of the add-on content types. Kotti includes
functionality for its own and add-own updates however; when needed, a database
"migration" can be run by the site adminstrator to translate and update older
entries to newer formats.
