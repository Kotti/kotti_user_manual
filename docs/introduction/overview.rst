The Nature of Kotti
===================

Kotti is a software system used to build websites and web applications. 

As a user, you don't have to know about the languages used, nor about the focus
on browser or server programming described below. You just use a website made
with Kotti.  However, understanding the nature of the software will stimulate
an appreciation of its strengths and build confidence in using it. Knowledge of
the general environment of website and web application software can help you
understand new ways we use software today, as compared to traditional desktop
apps, and the many "apps" available for the iPhone, Android, and mobile
devices.

Websites and web apps come in so many varieties. Broadly, for the modern World
Wide Web, several main development approaches are used:

* ``Web browser focus, with the server kept as a simple storage system.`` By web
  browser here, we refer to the common denominator formed by Mozilla Firefox,
  Google Chrome, Microsoft Internet Explorer, and several other choices of
  programs used to "surf the web." A focus on the web browser involves
  programming primarily in languages dedicated to the task, such as Javascript
  and CSS (cascading style sheets, for controlling the look of pages and
  components). Most of the computer processing in such a system happens on your
  computer, where the browser is running like any other program there, but
  occasionally talking to the server to send or fetch data. Speed of the system
  is very good for a well-designed system, because traffic back and forth to
  the server is reduced.
* ``Server focus, with a robust intelligent database system.`` Browsers are
  still the primary way of interacting with the user, and javascript and CSS
  can be important, but here larger portions of the user interface are fetched
  from and modified by the server, which contains the "brains" of the
  operation. The server software builds web pages and forms by interacting with
  a database via queries to update or fetch data, preparing the final result
  after inserting updated bits of information. Speed of the system can be very
  good overall, because the server stores frequently used parts of a website to
  reduce the amount of rebuilding needed. 
* ``Combinations`` that blur these two approaches.

Kotti uses the second approach primarily, in its default configuration, but has
the flavor of a combined approach, with the latest browser programming
techniques used for parts of the user interface, and with the programming
language ``Python`` forming the heart of the system on the server.  Kotti uses
an expressive programming system called ``Pyramid`` that forms a very good
foundation.  Kotti uses an interface to data called ``SQLAlchemy``, that
provides an intelligent way to work with a choice of solid databases.

Kotti forms a great platform for extending with browser programming of advanced
graphics and presentation features, combining the approaches described above in
the construction of web applications that go beyond the traditional CMS.

Your Kotti-based website could be an out-of-the-box default site with just a
few add-ons, or it could be a heavily customized site or web app. This user
manual covers use of a default configuration, but should be useful for learning
about any Kotti-based system.

.. Note:: What's the difference between a website and a web app? A website
          often appears as multiple pages, and may stress the presentation of
          static information, while including traditional web forms for
          accepting input from users. A web app in classic form will appear as
          a single page with displays that swap out for one another in place,
          working more like a desktop application on your computer.  These
          distinctions need not be limiting; a Kotti system can be built that
          has multiple pages, some of which can constitute "web apps" on their
          own. One page might present text and images for a static document.
          Another might involve dynamic graphics, "rich" interactivity, and
          multiple screens that swap out.

Design Goals
============

Kotti has marched through numerous revisions to become stable. A community
formed by a group of dedicated software developers has assembled. Many of the
developers have years of experience in CMS projects and in the languages used
in Kotti. The future looks bright for the adoption of Kotti for small and large
websites, for internal company systems, for social media, and many other
niches. It is a capable CMS on its own, and forms a solid base for programming
in the modern world of the web.

Programmers of Kotti try to:

* keep the core simple, using a *natural* design,
* use and re-use top-quality software components,
* write code that uses best practices for style and form,
* work collaboratively, using modern development tools, and
* test the software continuously.

The design of Kotti features content storage as something like an outline or
tree, where content is nested in a meaningful way.  This is the *natural*
design aspect, for which the Document content type is central.

Documents are added to a Kotti website in the way word-processor documents are
created on computers, but in the context of the web. Documents contain text and
may include images, files, and links to other documents.  Kotti's design makes
linking documents to one another happen automatically as the site structure is
built, document by document.  There are easy ways to make custom links from
documents to other content items, or to other websites. 

.. Note:: A document, thus, does double-duty, presenting its own textual and
          graphical content, while serving as the storage location for the
          associated images and files displayed or linked therein. A document
          is linked to its parent document, and may contain any number of child
          documents.

Consider a typical usage scenario for a fresh Kotti CMS website: You first add
documents for each main part of your website.  You then add documents within
those. You may add documents within documents within documents to form a deeply
nested structure.  Other content types can be considered secondary for
importance in organization, because you store images, files, and custom content
items within documents as the structure unfolds during site construction.
