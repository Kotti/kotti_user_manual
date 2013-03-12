The Nature of Kotti
===================

Kotti is a software framework used to build websites and web applications. 

As a user, you don't have to know about the languages used, nor about the focus
on browser or server programming described below. You just use a website made
with Kotti.  However, understanding the nature of the software will stimulate
an appreciation of its strengths and confidence in using it. Also, knowledge of
the general environment of website and web applications can help to demysify
new ways we all use software, from traditional desktop apps, to the many "apps"
available for the iPhone, Android, and mobile devices, to the web-oriented
systems like those built with Kotti.

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
language Python forming the heart of the system on the server.  Kotti uses an
expressive programming interface to the database called SQLAlchemy, providing
the "secret sauce" for working intelligently with data.

Kotti forms a great platform for extending with browser programming of advanced
graphics and presentation features, to allow a powerful combination of the
approaches described above.

Design Goals
============

Kotti has marched through numerous revisions to become stable. A community
formed by a group of dedicated software developers has assembled. Many of the
developers have years of experience in CMS projects and in the languages used
in Kotti. The future looks bright for the adoption of Kotti for small and large
websites, for internal company systems, for social media, and many other
niches. It is a capable CMS with high potential.

Programmers of Kotti try to:

* keep the core simple, using a *natural* design,
* use and re-use top-quality software components,
* write code that uses best practices for style and form,
* work collaboratively, using modern development tools, and
* test the software continuously.

The design of Kotti has content storage as something like an outline or tree,
where content is nested in a meaningful way.  This is the *natural* design
aspect.  The Document content type is the most important part of this concept.
Documents are added to a Kotti website in the way word-processor documents are
created on computers, but in the context of the web. Documents contain text and
may include images, files, and links to other documents.  Kotti's design makes
linking documents to one another happen automatically as the site structure is
built.  There are easy ways to make custom links between content items, or to
other websites. 

Reiterating the centrol role for the Document content type in organization, we
can describe a typical usage scenario. You add documents for each main part of
your website.  You add documents within those. If your site has a deep
structure, you add documents within documents within documents to form a deep
nested structure.  Everything else can be considered secondary for importance
in organization, because you store images, files, and custom content items
within documents as the structure unfolds during site construction. A given
document will have its own textual content, and will serve as the storage
location for the associated images and files displayed or linked there.
