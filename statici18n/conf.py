"""
Initializes the settings
"""
from django.conf import settings

from appconf import AppConf


class StaticFilesConf(AppConf):
    # The gettext domain to use when generating static files.
    DOMAIN = 'djangojs'
    # A list of packages to check for translations.
    PACKAGES = ('django.conf')
    # Controls the file path that generated static will be written into.
    ROOT = 'static'
    # Controls the directory inside STATICI18N_ROOT that compressed files will
    # be written to.
    OUTPUT_DIR = 'jsi18n'
    # The dotted path to the function that creates the filename
    FILENAME_FUNCTION = 'statici18n.utils.default_filename'
