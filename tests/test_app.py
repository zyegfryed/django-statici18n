import io
import os
import pytest

import django
from django.core import management
from django.template import Context, Engine
from django.utils import six
from django.utils import translation

LOCALES = ['en', 'fr', 'zh-Hans', 'ko-KR']


def get_template_from_string(template_code):
    engine_options = {}
    if django.VERSION >= (1, 9):
        engine_options = {
            'libraries': {
                'statici18n': 'statici18n.templatetags.statici18n',
            },
        }
    return Engine(**engine_options).from_string(template_code)


def to_locale(locale):
    if django.VERSION < (1, 10):
        return translation.to_locale(locale)
    return locale


@pytest.mark.usefixtures("cleandir")
def test_compile_all(settings):
    out = six.StringIO()
    management.call_command('compilejsi18n', verbosity=1, stdout=out)
    out.seek(0)
    lines = [l.strip() for l in out.readlines()]

    assert len(lines) == len(settings.LANGUAGES)
    for locale, _ in settings.LANGUAGES:
        assert "processing language %s" % to_locale(locale) in lines


LOCALIZED_CONTENT = {
    'en': 'django',
    'fr': '"Hello world!": "Bonjour \\u00e0 tous !"',
    'zh-Hans': '"Hello world!": "\\u5927\\u5bb6\\u597d\\uff01"',
    'ko-KR': '"Hello world!": "\\uc548\\ub155\\ud558\\uc138\\uc694!"'
}


@pytest.mark.usefixtures("cleandir")
@pytest.mark.parametrize('locale', LOCALES)
def test_compile(settings, locale):
    out = six.StringIO()
    management.call_command('compilejsi18n', verbosity=1, stdout=out,
                            locale=to_locale(locale))
    out.seek(0)
    lines = [l.strip() for l in out.readlines()]

    assert len(lines) == 1
    assert lines[0] == "processing language %s" % to_locale(locale)
    filename = os.path.join(
        settings.STATICI18N_ROOT, "jsi18n", to_locale(locale), "djangojs.js")
    assert os.path.exists(filename)
    with io.open(filename, "r", encoding="utf-8") as fp:
        content = fp.read()
        assert LOCALIZED_CONTENT[locale] in content


@pytest.mark.parametrize('locale', LOCALES)
def test_compile_no_use_i18n(settings, locale):
    """Tests compilation when `USE_I18N = False`.

    In this scenario, only the `settings.LANGUAGE_CODE` locale is processed
    (it defaults to `en-us` for Django projects).
    """
    settings.USE_I18N = False

    out = six.StringIO()
    management.call_command('compilejsi18n', verbosity=1, stdout=out,
                            locale=to_locale(locale))
    out.seek(0)
    lines = [l.strip() for l in out.readlines()]
    assert len(lines) == 1
    assert lines[0] == "processing language %s" % to_locale(locale)
    assert os.path.exists(os.path.join(
        settings.STATIC_ROOT, "jsi18n", to_locale(locale), "djangojs.js"))


@pytest.mark.parametrize('locale', ['en'])
@pytest.mark.parametrize('output_format', ['js', 'json'])
def test_compile_with_output_format(settings, locale, output_format):
    out = six.StringIO()
    management.call_command('compilejsi18n', verbosity=1, stdout=out,
                            locale=locale, outputformat=output_format)
    out.seek(0)
    lines = [l.strip() for l in out.readlines()]
    assert len(lines) == 1
    assert lines[0] == "processing language %s" % to_locale(locale)
    assert os.path.exists(os.path.join(
        settings.STATIC_ROOT, "jsi18n", locale, "djangojs.%s" % output_format))


@pytest.mark.usefixtures("cleandir")
def test_compile_locale_not_exists():
    out = six.StringIO()
    management.call_command('compilejsi18n', locale='ar', verbosity=1, stderr=out)
    assert out.getvalue() == ""


@pytest.mark.parametrize('locale', LOCALES)
def test_statici18n_templatetag(locale):
    template = """
    {% load statici18n %}
    <script src="{% statici18n LANGUAGE_CODE %}"></script>
    """
    template = get_template_from_string(template)
    assert template.render(Context({'LANGUAGE_CODE': locale})).strip() ==\
        '<script src="/static/jsi18n/%s/djangojs.js"></script>' % locale


@pytest.mark.usefixtures("cleandir")
@pytest.mark.parametrize('locale', LOCALES)
def test_inlinei18n_templatetag(locale):
    template = """
    {% load statici18n %}
    <script>{% inlinei18n LANGUAGE_CODE %}</script>
    """
    management.call_command('compilejsi18n')
    template = get_template_from_string(template)
    rendered = template.render(Context({'LANGUAGE_CODE': to_locale(locale)})).strip()
    assert 'var django = globals.django || (globals.django = {});' in rendered
    assert '&quot;' not in rendered
