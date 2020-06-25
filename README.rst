Clowning Around
===============

Intro
-----
There’s nothing quite as important as ensuring you’re punctual for any and all appointments made. This is a sign of respect and concern for the other parties time and needs. No being understands this quite as well as a clown. Your task, should you be so inclined, is to build a Django application, specifically for the time management needs of this world’s greatest child entertainers.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

The application, when complete, should be able to allow clowns, troupe leaders and clients to:

    Authenticate themselves as clowns, troupe leaders or clients

        - Clients to:

            - View their upcoming and past appointments (as an API endpoint)

            - Rate a past appointment with clown face emojis

        - Troupe leaders to:

            - Create appointments for clowns, assigned to a limited capacity troupe, managed by themselves

        - Clowns to:

            - View their appointments and change the current status of these appointments (upcoming, incipient, completed, cancelled)

            - Report an issue with an appointment (not a state change)

            - Request client contact details, with reason for request


Instructions
------------
All the above tasks should be completable through a collection of complete API endpoints. The application has a framework provided (based on https://github.com/pydanny/cookiecutter-django) with a fixture that contains dummy users you can use not only to test but also, use within your additional applications. The frontend provided can be ignored as a part of the cookiecutter and not the final application, which will be used exclusively through API endpoints. Your applications should include dummy data, which you can source from anywhere you’d like.

You only have two hours to complete the assignment, including any tasks you’d consider necessary to mark a feature/implementation/component complete. Should you not get around to doing anything, feel free to add TODO or NOTE comments to let us know you wanted to, but just didn’t get to.

We ask you provide your database as well. Simply add a dumpeddata.json file, using the ```docker-compose -f local.yml run --rm django python ./manage.py dumpdata --exclude auth.permission --exclude contenttypes > dumpeddata.json```
This dump may be added to the repository after the two hours have elapsed.

Please create a branch with your name (e.g. git checkout -b yeeshu-rastogi master) and make any changes there. Once finished, PR (pull request) into the master branch, to make it apparant what's been added or changed.

Have fun!

Project Specific Note
---------------------

The following are some things to help you get started

To get the provided datadump.json file into your database


```docker-compose -f local.yml run --rm django python ./manage.py loaddata datadump.json```

(``https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata``)


Settings
--------

Should there be an issue, crete the file. Not a whole new project.

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **superuser account**, use this command inside the django container::

    $ python manage.py createsuperuser

For convenience, you can run the following command from your terminal to create the user without having to open the shell in the container::
    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser


Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

.. _mailhog: https://github.com/mailhog/MailHog

If you'd prefer an old-school terminal view, I'd recommend sticking with Mailhog, unless you plan to have the Docker logs running while you dev.

Deployment
----------

The assignment is set for only two hours. You have only two hours to complete what you can. And no more. Doing more, with trash code, is still bad. Focus on what you can get done, and do it well!


Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html

That link is for any platform-specific, or additional commands you may need. The project has already been generated and a dummy data set provided.
