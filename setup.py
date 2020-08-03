# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.2'


setup(
    name='django-templatetags-ext',
    version=version,
    keywords='Django Template Tags TemplateTags Ext Extensions',
    description='Django TemplateTags Extensions',
    long_description=open('README.rst').read(),

    url='https://github.com/django-xxx/django-templatetags-extensions',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['django_templatetags_ext'],
    py_modules=[],
    install_requires=['monetary', 'screen', 'pysnippets'],
    include_package_data=True,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
