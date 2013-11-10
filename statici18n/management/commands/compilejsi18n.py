from __future__ import with_statement, print_function

import os
from optparse import make_option

from django.core.management.base import NoArgsCommand
from django.utils.translation import to_locale, activate


from statici18n.conf import settings
from statici18n.utils import get_filename
from statici18n.compat import javascript_catalog


class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list + (
        make_option('--locale', '-l', dest='locale',
                    help="The locale to process. Default is to process all."),
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
                         "Defaults to static/jsi18n.")
    )
    help = "Collect Javascript catalog files in a single location."

    def handle_noargs(self, **options):
        locale = options.get('locale')
        domain = options['domain']
        packages = options['packages'] or settings.STATICI18N_PACKAGES
        outputdir = options['outputdir']
        verbosity = int(options.get('verbosity'))

        if locale is not None:
            languages = [locale]
        else:
            languages = [to_locale(lang_code)
                         for (lang_code, lang_name) in settings.LANGUAGES]

        if outputdir is None:
            outputdir = os.path.join(
                settings.STATICI18N_ROOT, settings.STATICI18N_OUTPUT_DIR)

        for locale in languages:
            if verbosity > 0:
                print("processing language", locale)

            activate(locale)
            jsfile = os.path.join(outputdir, get_filename(locale, domain))
            basedir = os.path.dirname(jsfile)
            if not os.path.isdir(basedir):
                os.makedirs(basedir)

            src = javascript_catalog(locale, domain, packages)
            with open(jsfile, 'w') as f:
                f.write(src)
