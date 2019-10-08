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

    {{ price|fen2yuan }}

