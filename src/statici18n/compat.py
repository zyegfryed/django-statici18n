import os
import gettext as gettext_module

from django.conf import settings
from django.utils import importlib, six
from django.utils.text import javascript_quote
from django.utils.translation import to_locale

try:
    # Django >= 1.6
    from django.views.i18n import (get_javascript_catalog,
                                   render_javascript_catalog)

    def javascript_catalog(locale, domain, packages):
        catalog, plural = get_javascript_catalog(locale, domain, packages)
        return render_javascript_catalog(catalog, plural).content


except ImportError:
    # Django <= 1.5
    from django.views.i18n import (LibHead, LibFoot, LibFormatHead,
                                   LibFormatFoot, SimplePlural, InterPolate,
                                   PluralIdx, get_formats)

    LibFoot = LibFoot.replace('\x04', '\\x04')

    # This function is a ripoff of `django.views.i18n.javascript_catalog
    # with all the request specific code removed.
    def javascript_catalog(locale, domain, packages):
        packages = [p for p in packages
                    if p == 'django.conf' or p in settings.INSTALLED_APPS]
        default_locale = to_locale(settings.LANGUAGE_CODE)
        t = {}
        paths = []
        en_selected = locale.startswith('en')
        en_catalog_missing = True
        # paths of requested packages
        for package in packages:
            p = importlib.import_module(package)
            path = os.path.join(os.path.dirname(p.__file__), 'locale')
            paths.append(path)
        # add the filesystem paths listed in the LOCALE_PATHS setting
        paths.extend(list(reversed(settings.LOCALE_PATHS)))
        # first load all english languages files for defaults
        for path in paths:
            try:
                catalog = gettext_module.translation(domain, path, ['en'])
                t.update(catalog._catalog)
            except IOError:
                pass
            else:
                # 'en' is the selected language and at least one of the
                # packages listed in `packages` has an 'en' catalog
                if en_selected:
                    en_catalog_missing = False
        # next load the settings.LANGUAGE_CODE translations if it isn't
        # english
        if default_locale != 'en':
            for path in paths:
                try:
                    catalog = gettext_module.translation(
                        domain, path, [default_locale])
                except IOError:
                    catalog = None
                if catalog is not None:
                    t.update(catalog._catalog)
        # last load the currently selected language, if it isn't
        # identical to the default.
        if locale != default_locale:
            # If the currently selected language is English but it
            # doesn't have a translation catalog (presumably due to
            # being the language translated from) then a wrong language
            # catalog might have been loaded in the previous step. It
            # needs to be discarded.
            if en_selected and en_catalog_missing:
                t = {}
            else:
                locale_t = {}
                for path in paths:
                    try:
                        catalog = gettext_module.translation(
                            domain, path, [locale])
                    except IOError:
                        catalog = None
                    if catalog is not None:
                        locale_t.update(catalog._catalog)
                if locale_t:
                    t = locale_t
        src = [LibHead]
        plural = None
        if '' in t:
            for l in t[''].split('\n'):
                if l.startswith('Plural-Forms:'):
                    plural = l.split(':', 1)[1].strip()
        if plural is not None:
            # this should actually be a compiled function of a typical
            # plural-form: Plural-Forms: nplurals=3; plural=n%10==1 &&
            # n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 ||
            # n%100>=20) ? 1 : 2;
            plural = [el.strip()
                      for el in plural.split(';')
                      if el.strip().startswith('plural=')][0].split('=', 1)[1]
            src.append(PluralIdx % plural)
        else:
            src.append(SimplePlural)
        csrc = []
        pdict = {}
        for k, v in t.items():
            if k == '':
                continue
            if isinstance(k, six.string_types):
                csrc.append("catalog['%s'] = '%s';\n" %
                            (javascript_quote(k), javascript_quote(v)))
            elif isinstance(k, tuple):
                if k[0] not in pdict:
                    pdict[k[0]] = k[1]
                else:
                    pdict[k[0]] = max(k[1], pdict[k[0]])
                csrc.append("catalog['%s'][%d] = '%s';\n" %
                            (javascript_quote(k[0]), k[1], javascript_quote(v)))
            else:
                raise TypeError(k)
        csrc.sort()
        for k, v in pdict.items():
            src.append("catalog['%s'] = [%s];\n" %
                       (javascript_quote(k), ','.join(["''"] * (v + 1))))
        src.extend(csrc)
        src.append(LibFoot)
        src.append(InterPolate)
        src.append(LibFormatHead)
        src.append(get_formats())
        src.append(LibFormatFoot)
        src = ''.join(src)
        return src
