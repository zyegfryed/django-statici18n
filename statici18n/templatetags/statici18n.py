from __future__ import absolute_import
import os
from django import template

try:
    from django.contrib.staticfiles.templatetags.staticfiles import static
except ImportError:
    from staticfiles.templatetags.staticfiles import static

from statici18n.conf import settings
from statici18n.utils import get_filename

register = template.Library()


@register.simple_tag
def statici18n(locale):
    """
    A template tag that returns the URL to a Javascript catalog
    for the selected locale.

    Behind the scenes, this is a thin wrapper around staticfiles's static
    template tag.
    """
    path = os.path.join(settings.STATICI18N_OUTPUT_DIR,
        get_filename(locale, settings.STATICI18N_DOMAIN))
    return static(path)
