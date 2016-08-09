from __future__ import with_statement

import io
import os
import json
from optparse import make_option

from django.core.management.base import NoArgsCommand
from django.utils.translation import to_locale, activate
from django.utils.encoding import force_text

from statici18n.conf import settings
from statici18n.utils import get_filename

import django
if django.VERSION >= (1, 6):
    # Django >= 1.6
    from django.views.i18n import (get_javascript_catalog,
                                   render_javascript_catalog,
                                   get_formats)
else:
    # Django <= 1.5
    from statici18n.compat import (get_javascript_catalog,
                                   render_javascript_catalog,
                                   get_formats)


class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list + (
        make_option('--locale', '-l', dest='locale',
                    help="The locale to process. Default is to process all "
                         "but if for some reason I18N features are disabled, "
                         "only `settings.LANGUAGE_CODE` will be processed."),
        make_option('-d', '--domain',
                    dest='domain', default=settings.STATICI18N_DOMAIN,
                    help="Override the gettext domain. By default, "
                         " the command uses the djangojs gettext domain."),
        make_option('-p', '--packages', action='append', default=[],
                    dest='packages',
                    help="A list of packages to check for translations. "
                         "Default is 'django.conf'. Use multiple times to "
                         "add more."),
        make_option('-o', '--output', dest='outputdir', metavar='OUTPUT_DIR',
                    help="Output directory to store generated catalogs. "
                         "Defaults to static/jsi18n."),
        make_option('-f', '--format', dest='outputformat', metavar='OUTPUT_FORMAT',
                    choices=['js', 'json'], default='js',
                    help="Format of the output catalog. Options are: js, json "
                         "Defaults to js."),
    )
    help = "Collect Javascript catalog files in a single location."

    def __init__(self):
        super(NoArgsCommand, self).__init__()
        if hasattr(self, 'requires_system_checks'):
            self.requires_system_checks = False

    def _create_javascript_catalog(self, locale, domain, packages):
        activate(locale)
        catalog, plural = get_javascript_catalog(locale, domain, packages)
        response = render_javascript_catalog(catalog, plural)

        return force_text(response.content)

    def _create_json_catalog(self, locale, domain, packages):
        activate(locale)
        catalog, plural = get_javascript_catalog(locale, domain, packages)
        data = {
            'catalog': catalog,
            'formats': get_formats(),
            'plural': plural,
        }

        return force_text(json.dumps(data, ensure_ascii=False))

    def _create_output(self, outputdir, outputformat, locale, domain, packages):
        outputfile = os.path.join(outputdir, get_filename(locale, domain, outputformat))
        basedir = os.path.dirname(outputfile)
        if not os.path.isdir(basedir):
            os.makedirs(basedir)

        if outputformat == 'js':
            data = self._create_javascript_catalog(locale, domain, packages)
        elif outputformat == 'json':
            data = self._create_json_catalog(locale, domain, packages)
        else:
            raise NotImplementedError("Unknown format %s" % (outputformat))

        with io.open(outputfile, "w", encoding="utf-8") as fp:
            fp.write(data)

    def handle_noargs(self, **options):
        locale = options.get('locale')
        domain = options['domain']
        packages = options['packages'] or settings.STATICI18N_PACKAGES
        outputdir = options['outputdir']
        outputformat = options['outputformat']
        verbosity = int(options.get('verbosity'))

        if locale is not None:
            languages = [locale]
        elif not settings.USE_I18N:
            languages = [settings.LANGUAGE_CODE]
        else:
            languages = [to_locale(lang_code)
                         for (lang_code, lang_name) in settings.LANGUAGES]

        if outputdir is None:
            outputdir = os.path.join(settings.STATICI18N_ROOT,
                                     settings.STATICI18N_OUTPUT_DIR)

        for locale in languages:
            if verbosity > 0:
                self.stdout.write("processing language %s\n" % locale)

            self._create_output(outputdir, outputformat, locale, domain, packages)
