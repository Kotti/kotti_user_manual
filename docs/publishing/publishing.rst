Publishing Content
------------------

Recall the two workflow states in the default Kotti website: Private and
Public. All of the content we added to the fruit stand website is in the
Private state. So, if we log out, we don't see anything but the front page:

.. Image:: ../images/not_logged_in.png

We don't see the "About" page, nor any of the rest, because anonymous viewers
can only see Public content. Private content is invisible to them.

We can publish content by changing the state of items from Private to Public by
several methods. The quickest way for single items is to use the pulldown menu
on the left side of the editor bar:

.. Image:: ../images/state_menu.png

If we log back in and do that for "About," "Featured Fruits," "Fruit
Rootstock," and "Fruits" main content items, and then log back out, we now
can see those content items in anonymous view:

.. Image:: ../images/published.png

Recursive Publishing
--------------------

The content of our fruit stand website does not have a deeply nested structure,
because there isn't much content on the site yet. After more work, however,
there could be sections within sections, made by a mix of documents, images,
files, and custom content items. Kotti lets you change the publication state of
entire sections by using a powerful feature called recursion::

    recursion - The root word is recur, "occur again, periodically, or
                repeatedly," and in the context used for a Kotti website, we
                mean "walk through all nested content within a section of the
                website, performing an operation on all items."

Consider a case where you would like to publish a large new section called
"Fruit Tree Care and Feeding," all contained within a main document by that
name. There are documents for subsections, and there are many images, pdf
files, documents with tables, etc., within them. It would be impractical to
click on each content item, changing Private to Public for each one. This is
where recursion comes in. You get to this feature under the "Contents" view,
which you would visit for the "Fruit Tree Care and Feeding" document.  The
bottom row of buttons has a "Change State" button:

.. Image:: ../images/contents_action_buttons.png

When the "Change State" button is clicked, you are given a choice of the state
change to perform, e.g. Private -> Public, and there is a checkbox for
recursive.  Check this to apply the operation to all content, no matter how
deeply nested within the containing content item. The reverse operation can be
just as important: you may wish to "unpublish" an entire section with a
recursive Public -> Private change.

If you do not choose the recursive option when doing a state change, the change
will be applied only to the content item itself, not any contained items.
