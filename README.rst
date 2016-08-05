cmsplugin-markdown
==================

This is a plugin for django-cms that aims to replace the standard text plugin
with it's WYSIWYG editors. With cmsplugin-markdown you can write your content
in Markdown using EpicEditor (http://oscargodson.github.com/EpicEditor/)

Installation
------------

You need to install the following prerequisites in order to use this app::

    pip install Django
    pip install django-cms
    pip install Markdown
    pip install django-markwhat

If you want to install the latest stable release from PyPi::

    $ pip install cmsplugin-markdown

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/cmsplugin-markdown.git#egg=cmsplugin_markdown

Add ``cmsplugin_markdown`` and ``django_markwhat`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'django_markwhat',
        'cmsplugin_markdown',
    )

Don't forget to migrate your database::

    ./manage.py migrate cmsplugin_markdown

Usage
-----

Just go to the page admin of django-cms (or the Entries admin of
cmsplugin-blog) and add a markdown plugin to a placeholder. It should be pretty
much self-explanatory.

Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ git co -b feature_branch master
    # Implement your feature and tests
    # Describe your change in the CHANGELOG.txt
    $ git add . && git commit
    $ git push origin feature_branch
    # Send us a pull request for your feature branch

Roadmap
-------

Check the issue tracker on github for milestones and features to come.

License
-------

**Major components:**

* EpicEditor: [MIT license](https://github.com/OscarGodson/EpicEditor/blob/develop/LICENSE)
* Everything else: [MIT license](https://github.com/bitmazk/cmsplugin-markdown/blob/master/LICENSE)
