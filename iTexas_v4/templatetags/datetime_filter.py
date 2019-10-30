# -*- coding: utf-8 -*-
"""Application filter for `datetime`_ 24 hours.

.. _datetime: https://docs.python.org/2/library/datetime.html
"""

from django import template
from datetime import date, timedelta

register = template.Library()


@register.filter(name='format_datetime')
def format_datetime(value):
    if value is not None:
        hours, rem = divmod(value.seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        return '{:02d}:{:02d}'.format(hours, minutes)
    else:
        return '-'

