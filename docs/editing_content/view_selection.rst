View Selection
==============

The default view for a content item is set by the system for Document, Image,
and File, and by custom add-on software for custom types. If a content item
contains other items, a list of the items can be seen in the Contents view.

Recall that we added fruit images for to the "Fruits" document, for which we
saw a listing via the "Contents" view. Viewing the fruits in this way is
useful, but it requires two steps:

1. Clicking on the "Fruits" document, which will only show a title and
   description, because we gave it no body text, since it is a container of
   fruit images.
2. Then clicking on "Contents" to see the contained fruit images.

We would rather make it so that when "Fruits" is clicked, it shows the list of
contained items immediately. We do this by setting the default view for the
"Fruits" document to "Folder view" ("Folder view" is about to be clicked in
this view, and it will then show the check mark):

.. Image:: ../images/set_default_view.png

Now when we click directly on the "Fruits" document, we see a list view:

.. Image:: ../images/fruits_view.png

Should you later want to change the default view back to normal document view,
you can set the it back to "Default view". This could happen if a document
contains other documents, and is used as a simple list for a time, having
default view set to "Folder view," but then the contained documents are removed
for some reason. The original document could then have its default view set
back to "Default view" and perhaps its description revised and body text
entered or updated.

Or, perhaps the main document containing other documents, images, or files,
has a custom body treatment, complete with links to the contained items. In
this case, the default view would be kept as "Default view" to show the title,
description, and custom body. We could do this for "Fruits" but consider the
advantage of not maintaining a custom body with links -- with default view set
to "Folder view," anytime we add or delete a fruit image, the list view is
automatically up-to-date.
