==============================
django-templatetags-extensions
==============================

Django TemplateTags Extensions

Installation
============

::

    pip install django-templatetags-ext


Settings.py
===========

::

    INSTALLED_APPS = (
        ...
        'django_templatetags_ext',
        ...
    )


Usage
=====

::

    {% load templatehelper %}

    {{ googol|googolformat }}
    {{ googol|googolformat:ndigits }}

    {{ googol|googolformat2 }}
    {{ googol|googolformat2:ndigits }}

    {{ price|fen2yuan }}
    {{ price|fen2yuan:ndigits }}

    {{ value|truncatechars2:length }}
    {{ value|truncatechars2:'length,truncate' }}

    {{ value|truncatewidth:length }}
    {{ value|truncatewidth:'length,truncate' }}

    {{ value|remove_line_break }}
    {{ value|remove_line_break:repl }}

