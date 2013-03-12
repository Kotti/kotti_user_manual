Workflow Policies
=================

The term used for the setup for user and roles and related functionality is
``workflow``.  You do not need to create a workflow policy to use a Kotti
website. If you are the sole user of the website, roles are not needed -- you
are ``it``! But when multiple people are involved, discrete roles can be
useful. Even then, a custom workflow is not needed, because as user groups are
created by the Admin user, a simple defacto workflow is created using the
built-in states, Private and Public.

A custom workflow is needed when there is more involved in the process of
creating and editing content items.

A workflow is constituted by a set of policies created for a given CMS setup,
wherein user groups and roles are defined, and relationships and
responsibilities established by creation of workflow states that expand upon
Private and Public. These could include Pending, Postponed, Scheduled,
Ready-For-Circulation, Needs-Full-Review, etc., depending on specific needs. As
these state names suggest, this is an area where creativity can help to build a
fine-grained system.

For example, a manufacturing operation, e.g. for custom clothing, could have an
in-house Kotti CMS for documenting and controlling flow of project work. The
designers of the workflow would need to understand the physical layout of the
manufacturing area and would need to plan for work schedules and timing
constraints. They would create user roles for different stages of manufacture
and assembly work, and custom content types with web forms that people would
use to enter data into computer terminals on the work floor. A sequential flow
of work stages would develop, starting with the initial work on the project
piece, followed by quality control checks before it moves to the next
workstation area. A given workstation could check a list of project pieces and
where they are in the queue. The names of the workflow states and transitions
might look like this:

.. Image:: ../images/manufacturer_workflow.png

Think of documents tied to individual project pieces by serial number, that
would be marked as the items are carried through the process.

For a similar example, Kotti could be used for a video production shop, which
might have roles in the workflow such as "Ingestion," which would have people
working with raw video in the first processing steps, along with roles for
"Color Correcting," "Titles," "Special Effects," etc. And the states used along
the way could include "Raw footage," "Initial Compression Good,", "Initial
Compression Failed," "Color Corrected," "Ending Credits Added," etc. 
