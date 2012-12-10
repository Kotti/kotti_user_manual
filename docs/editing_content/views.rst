=====
Views
=====

Editing content uses the same, or very similar forms as the Add view. For a
Document you see the title and description at the top, then the tags, then the
body. You see the same word processor-like user interface to change the body.
For an Image, you see the title, description, tags, then a button to change the
existing image -- to upload a new version of the image or an altogether new
image.  The edit view for a File is exactly like that for an Image: there is a
button to upload a new version of the file or an altogether new file. The edit
view for custom content types is what you expect, following this general
pattern.

After an item of content has been added, you may choose View, Contents, or
Edit::

    - View - the item in normal view
    - Contents - a list of contained items (empty if there are none)
    - Edit - the Edit form for the content item

View and Edit views are straightforward counterparts. The Contents view is
dedicated to showing a list of contained items, but it is more than that,
offering several "power" features.

Creating Links
--------------

You often want to make links from one document to another.  This is easy. When
adding or editing the body of a document, select the word or phrase that you
would like to make into a link, then click the button to add a link, then
browse the website to find the target document for the link. Kotti will
immediately format the link.  You can use the same procedure to add a link to
an external web page, pasting in the URL of the external web page.

We need to add a link to our "Fruits" document in the "About" document. We do
this by clicking on "About," then clicking "Edit" in the editor bar:

.. Image:: ../images/about_document_edit.png

Then, in the body add the following sentence::

    Our fruit stand has many fruits.

Then select the words "fruit stand" with your mouse. Then click the icon that
looks like links of a chain. You will see the link widget:

.. Image:: ../images/about_document_adding_link_browse.png

Click the browse button to the right of the URL entry field, and then find the
"Fruits" document and click on it:

.. Image:: ../images/about_document_adding_link_fruits_document.png

After saving the document, you will have a link from the "About" page to the
"Fruits" document:

.. Image:: ../images/about_document_with_link_to_fruits_document.png
