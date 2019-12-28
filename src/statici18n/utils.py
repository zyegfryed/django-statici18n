try:
    from collections.abc import Sequence
except ImportError:
    from collections import Sequence
import os

from importlib import import_module
import six

from statici18n.conf import settings


def get_mod_func(callback):
    """
    Converts 'django.views.news.stories.story_detail' to
    ('django.views.news.stories', 'story_detail')
    """
    try:
        dot = callback.rindex('.')
    except ValueError:
        return callback, ''
    return callback[:dot], callback[dot + 1:]


def get_filename(*args, **kwargs):
    try:
        mod_name, func_name = get_mod_func(
            settings.STATICI18N_FILENAME_FUNCTION)
        _filename_func = getattr(import_module(mod_name), func_name)
    except (AttributeError, ImportError) as e:
        raise ImportError("Couldn't import filename function %s: %s" %
                          (settings.STATICI18N_FILENAME_FUNCTION, e))
    return _filename_func(*args, **kwargs)


def default_filename(language_code, domain, output_format='js'):
    return os.path.join(language_code, '%s.%s' % (domain, output_format))


def legacy_filename(locale, domain, output_format='js'):
    from django.utils.translation.trans_real import to_language
    return os.path.join(to_language(locale), '%s.%s' % (domain, output_format))


def get_packages(packages):
    if packages == 'django.conf':
        return None

    if isinstance(packages, six.string_types):
        return packages

    if isinstance(packages, Sequence):
        return '+'.join(packages)
