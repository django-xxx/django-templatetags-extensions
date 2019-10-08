# django-templatetags-extensions
Django TemplateTags Extensions

## Installation
```shell
pip install django-templatetags-ext
```

## Settings.py
```python
INSTALLED_APPS = (
    ...
    'django_templatetags_ext',
    ...
)
```

## Usage
```python
{% load templatehelper %}

{{ price|fen2yuan }}
```
