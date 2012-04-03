import os

from django.utils.importlib import import_module

from statici18n.conf import settings

_filename_func = None


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
    global _filename_func
    if _filename_func is None:
        try:
            mod_name, func_name = get_mod_func(
                settings.STATICI18N_FILENAME_FUNCTION)
            _filename_func = getattr(import_module(mod_name), func_name)
        except (AttributeError, ImportError), e:
            raise ImportError("Couldn't import filename function %s: %s" %
                              (settings.STATICI18N_FILENAME_FUNCTION, e))
    return _filename_func(*args, **kwargs)


def default_filename(locale, domain):
    return os.path.join(locale, '%s.js' % domain)
