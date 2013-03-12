Users and Roles
===============

A website is usually a presentation of text and images and other content
available for view by anyone. The content of the website is added by any number
of ways to build websites, but there is often no concept of "logging in" to see
content. The content is viewable by all who visit the website. This can be
called ``anonymous`` viewing, and the general website visitor can be called an
anonymous user.

A CMS does involve the concept of "logging in," at least for the person adding
content, and it involves the concept of having content in public vs. private
state: public, for allowing open viewing by the anonymous user, as for a
typical website, and private, for restricting viewing to the "logged in" user.
Once a user has logged in, they can be called an ``authenticated`` user,
because they have entered their correct username and password.

.. Image:: ../images/anonymous_vs_authenticated.png

In its simplest form, Kotti allows a special user, called the Admin user, to
log in and add and edit content. In such a simple Kotti website the person who
will be adding content, is the Admin user. The Admin user has full rights to do
anything to the website.

For a larger Kotti website, where several people add content, the Admin user
may create accounts for other people. One common approach is to divide the
website into several top-level sections that different people manage. For
example, imagine a scenario where Joe, Sally, and Xavier are the content
managers for a musical act agency. First the Admin user logs in (perhaps the
Admin user is one of them; perhaps it is a fourth person), creates the three
accounts, then sends emails with user names and passwords.  The Admin user
creates three top-level sections of the website, notifying Joe, Sally, and
Xavier about their responsibilities: Joe for the ``Prospects`` section, Sally
for the ``Existing Clients`` section, and Xavier for the ``Legal Affairs``
section.  The Admin user assigns rights to these three areas by creating three
user groups: prospects, existing_clients, and legal_affairs. Then, by setting
the respective groups as owners of the three website sections, a scheme for
organization and responsibility is established.  Additional people can be added
by simply assigning them to a given group. For example, if Judy works with
Xavier on the legal team, the Admin user creates a new account for Judy, then
assigns her to the legal_affairs group, then emails her about the new account
and her responsibilities.  Judy and Xavier will both have rights to add and
edit content in the ``Legal Affairs`` section. Joe, Sally, Xavier, and Judy
share responsibilities like this:

.. Image:: ../images/roles_music_agency.png

Kotti includes a user registration system that can be open for general users to
sign up. This is useful for social media websites that seek out membership. It
can also be useful for a larger organization or company to facilitate the
account creation process. The system can be configured so that new registrants
automatically receive a confirmation email. These new users can also be
automatically assigned to a group by programming.

Many different scenarios are possible for creating roles for users of the CMS.
For a large multi-level organization, user groups can be created that mimic
that organization. Rights can be assigned so that users in one group are
restricted in what they can view, what they can add and edit. In the classic
example, a newspaper could have user groups for ``reporters``,
``photographers``, ``editors``, ``managers``, etc. Each would have specific
responsibilities and rights.  A ``reporter`` can only write and compile
articles, along with ``photographers``.  Together they could belong to a
"Creators" group. An ``editor`` can edit their work, but is not allowed to
publish.  Only ``managers`` can publish content.

.. Image:: ../images/newspaper_workflow.png

Even a small business with a handful of employees, or a small non-profit with
just a few members, can benefit from some form of structure like this.
