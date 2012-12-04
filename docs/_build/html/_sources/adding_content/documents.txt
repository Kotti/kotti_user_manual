=========
Documents
=========

Adding content to a new Kotti website usually involves adding top-level documents, for
main sections of the website, followed by adding documents within these sections. Files
and images are added in course, where they are needed within the sections. Before you
know it, a nested structure of documents is complete. Kotti makes this a very natural
process, principally through the design of the Document content type.

.. Image:: ../images/add_menu.png

The web form for adding a Document has the title at the top, then the
description, then the body. The title and description have simple text fields
for keyboard entry. The body has a special widget, something like that seen in
Word processor software, for formatting text, headings, and paragraphs. Each of
these Document properties has its own special nature.

Title
-----

The title of a document is, of course, very important. Kotti is smart about how
titles are transformed to work as key parts of the "web address" of each
document. You see web addresses everywhere as you use the Internet.
www.google.com is a web address, and so is www.bbc.com. And so is
www.bbc.com/news. And so is www.bbc.com/news/asia. These web addresses are
called URLs, for Universal Resource Locator, the official name that goes back
to the creation of the World Wide Web. When you add a Document, you don't have
to worry so much about the rules of making good URLs, because Kotti takes care
it.

The following table shows what the URLs for titles of documents added to a
website section for recipes:

========================= ====================================================
        Title                                      URL
------------------------- ----------------------------------------------------
Baked Alaska              www.somewebsite.com/recipes/baked-alaska
Pumpkin-Ginger Cupcakes   www.somewebsite.com/recipes/pumpkin-ginger-cupcakes
Granny Carol's Brownies   www.somewebsite.com/recipes/granny-carols-brownies
Walnut/Pecan/Almond Mix   www.somewebsite.com/recipes/walnut-pecan-almond-mix
========================= ====================================================

You see that blanks are replaced by dashes. Special characters such as
apostrophes and backslashes are ignored, and so on. Look at the URLs again.
Kotti ensures that they are clean and simple, and that you can make the titles
however you want without worry.

The title is mandatory. You have to have one to make the URL for the document.

Description
-----------

Kotti follows the tradition of CMS software in the handling of descriptions.
Descriptions are plain text-only. You can't make some words bold. You can't
make paragraphs. These restrictions may cramp your style, literally, but they
are in place to force a simplicity. If you need special formatted text, put it
in the body. Make good descriptions. Complete sentences with proper punctuation
are great. Use words that fit the item, thinking of keywords that match search
text strings you imagine people would use. Keep it fairly short.

The description is optional, but it is a good habit to write descriptions,
because it helps to provide searchable text.

Tags
----

Tags are keywords that are unique site-wide. If you add recipes to your site,
create tags for different food types: desserts, brownies, cakes, etc. The tags
entry field is smart. After you have typed a few characters, for example "bro"
in brownies, Kotti will check the existing set of tags for the site for
matches, and if it finds a pre-existing tag, or several tags, that begin with
"bro" you will see a small pop-up display of those tags to choose one. When you
have entered a new tag or selected an existing tag, hit the tab key to add
another.

Tags are optional, but as for descriptions, it is a good habit to add them,
because doing so provides an immediate organization of content that can be
searched categorically. If you see the brownies tag anywhere on an item, click
it to seach for all content that has been tagged for the brownies tag.
Likewise, use the general search to find content associated with multple tags
by using a search string such as "brownies cakes" to find all content items
that have been tagged with either the brownies or cakes tags.

Body
----

The Document body is where you add the real content. Add text, format words for
bold, italic, underline, and other formatting options. Select a paragraph and
indent it. Select several paragraphs and make a bulleted list. Create headings.
You have the normal range of features available in word processing software.

But you have more. Make a blank line and put the text cursor on the blank lind.
Click the button to add an image and browse to find a photograph on your local
computer. When you add the image, Kotti will put it at the position of the text
cursor on the blank line. You can do the same for adding an image at the
beginning of a paragraph. Click to place the text cursor at the first
character, on the first line of the paragraph, then click the button to add the
image. The text will wrap around the image by default, but you have several
image-to-text formatting options. This also works like a word processing
software, whereby you can embed images in a document.

Once you have added several documents, perhaps following an outline to build a
nested structure of documents, Kotti will handle linking the documents together
in its menu and breadcrumbs system. You see the main sections displayed across
the top, in the toolbar. You see the path to the current document in the
breadcrumbs display above the title. This automatic linking is great, but you
often want to make links to specific documents as you write new documents. This
is easy. Select the word or phrase that you would like to make into a link,
then click the button to add a link, then browse the website to find the target
document for the link. Kotti will immediately format the link. You can use the
same procedure to add a link to an external web page -- instead of browsing for
a document on the Kotti website, type or paste in the URL of the external web
page.
