# -*- coding: utf-8 -*-

from django.template import Library
from django.forms.boundfield import BoundField

__author__ = 'Yehenii Onoshko'

register = Library()


@register.filter(name='addclass')
def addclass(field, css_class):
    """

    Filter - Adds CSS class to item
    Usage:

    {{ some_element|addclass:'cssclass' }}

    :param field: django.forms.widgets.Widget
    :param css_class: str
    :return: django.forms.widgets.Widget
    """
    # print(type(field))
    if isinstance(field, BoundField):
        classes = field.field.widget.attrs.get('class', None)
        if classes:
            classes = field.field.widget.attrs['class'].split()
            classes.append(css_class)
            css_class = " ".join(classes)
    return field.as_widget(attrs={'class': css_class})


@register.filter(name='addplaceholder')
def add_placeholder(field, placeholder):
    return field.as_widget(attrs={'placeholder': placeholder})
