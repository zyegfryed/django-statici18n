"""
Initializes the settings
"""
from django.conf import settings

from appconf import AppConf


class StaticFilesConf(AppConf):
    DOMAIN = 'djangojs'
    PACKAGES = ('django.conf')
    ROOT = 'static'
    OUTPUT_DIR = 'jsi18n'
    FILENAME_FUNCTION = 'statici18n.utils.default_filename'
