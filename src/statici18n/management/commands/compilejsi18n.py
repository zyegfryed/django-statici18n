from __future__ import with_statement

from collections import OrderedDict
from cStringIO import StringIO
import io
import os
from optparse import make_option

from django.core.management.base import NoArgsCommand
from django.utils.translation import to_locale, activate
from django.utils.encoding import force_text

try:
    from django.contrib.staticfiles.storage import staticfiles_storage
except ImportError:
    from staticfiles.storage import staticfiles_storage

from statici18n.conf import settings
from statici18n.utils import get_filename, get_path

import django
if django.VERSION >= (1, 6):
    # Django >= 1.6
    from django.views.i18n import (get_javascript_catalog,
                                   render_javascript_catalog)
else:
    # Django <= 1.5
    from statici18n.compat import (get_javascript_catalog,
                                   render_javascript_catalog)


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

    def __init__(self):
        super(NoArgsCommand, self).__init__()
        if hasattr(self, 'requires_system_checks'):
            self.requires_system_checks = False

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

        if outputdir is not None:
            def write_file(locale, content):
                jsfile = os.path.join(outputdir, get_filename(locale, domain))
                basedir = os.path.dirname(jsfile)
                if not os.path.isdir(basedir):
                    os.makedirs(basedir)

                with io.open(jsfile, "w", encoding="utf-8") as fp:
                    fp.write(content)

            def post_process():
                pass

        else:
            paths = OrderedDict()

            def write_file(locale, content):
                path = get_path(locale, domain)
                paths[path] = (staticfiles_storage, path)
                staticfiles_storage.save(path,
                                         StringIO(content))

            def post_process():
                if not hasattr(staticfiles_storage, 'post_process'):
                    return

                processor = staticfiles_storage.post_process(paths)
                for original_path, processed_path, processed in processor:
                    if processed:
                        self.stdout.write("Post-processed file %s as %s" %
                                         (original_path, processed_path))

        for locale in languages:
            if verbosity > 0:
                self.stdout.write("processing language %s\n" % locale)

            activate(locale)
            catalog, plural = get_javascript_catalog(locale, domain, packages)
            response = render_javascript_catalog(catalog, plural)

            write_file(locale, force_text(response.content))

        post_process()
