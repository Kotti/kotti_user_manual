========
Overview
========

A website is a website is a website. Not.

For the modern day World Wide Web, websites are built using several main
development approaches, including:

* Web browser focus, with the server kept as a simple storage system.
* Server focus, with a robust database storage system.
* Combinations that blur these two approaches.

Kotti uses the second approach mainly, but has the flavor of a combined
approach, with the latest browser programming techniques used for parts of the
user interface, and with the programming language Python forming the heart of
the system on the server, backed by a powerful database engine.

As a user, you don't have to know about the languages used, nor the focus on
browser or server programming -- You just use the website. However,
understanding the nature of the software will help you to appreciate it, to
build confidence in it.

The choice of approach made by Kotti, and the software components used, reflect
several goals desired by the seasoned content management system professionals
and software developers who make Kotti:

* Keep the core simple, using a natural design.
* Use and re-use best-of-breed software components.
* Write code that uses best practices for style and form.
* Work collaboratively, using modern development tools.
* Test the software continuously.

Kotti has marched through numerous revisions to become stable, and a group of
dedicated software developers has assembled. The future looks bright for the
adoption of Kotti for small and large websites, for internal company systems,
for social media, and many other niches. It is a capable CMS.

The design of Kotti has content storage as something like an outline or tree,
where content is nested in a meaningful way.  This is the natural aspect. The
Document content type is the most important part of this concept. Documents are
added to a Kotti website in the way word-processor documents are created, but
in the context of the web. Documents contain text and may include images,
files, and links to other documents.  Kotti's design makes linking documents to
one another easy.

A fresh default Kotti website looks simple enough:

.. Image:: ../images/not_logged_in.png

There is a header area with a toolbar, which has the site "brand" on the left
and a Search box on the right.  There is a Welcome statement, instructions for
logging in, configuring the site, viewing a list of available add-ons, and
viewing documentation. The amusing footer is a signature of a software system
called Pyramid that Kotti uses as a foundation.

All of this will change when the website is configured and initial content is
added.

Getting Started With a New Site
-------------------------------

In addition to the front page with general information, Kotti creates an
initial website with a single document called "About" that has a photograph of
some airplanes and placeholder text. Both of these need to be changed for a new
website.

For the website associated with this user manual we will add content for a
fruit stand.  We will replace the "About" page with information about the fruit
stand offerings and schedule, and we will put introductory information on the
front page. We will add a Document called "Fruits," and to it we will add
images of the fruits for sale.  We will tag the fruit images for fruit
categories to which they belong.  This will be enough to demonstrate Kotti's
main features.

For the first actual task, let's delete the default "About" page. We are logged
in, so we can see it. Notice that it is in the Private state (left side of
screen), so it was not visible before we logged in.

.. Image:: ../images/default_about.png

Now that we have it in view, we have certain actions available via the
"Actions" pull-down menu, one of which is "Delete":

.. Image:: ../images/default_about_actions_menu.png

When we click the "Actions" menu, and the "Delete" choice, we get a
confirmation page:

.. Image:: ../images/default_about_delete_confirmation.png
