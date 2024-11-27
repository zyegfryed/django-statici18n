import io
import os
import pytest
import re

from django.core import management
from django.template import Context, Engine
from django.utils.translation import to_language

from statici18n.utils import default_filename


LOCALES = ["en", "fr", "zh_Hans", "ko_KR"]
LANGUAGES = [to_language(locale) for locale in LOCALES]


def get_template_from_string(template_code):
    engine_options = {
        "libraries": {
            "statici18n": "statici18n.templatetags.statici18n",
        },
    }
    return Engine(**engine_options).from_string(template_code)


@pytest.mark.usefixtures("cleandir")
def test_compile_all(settings):
    out = io.StringIO()
    management.call_command("compilejsi18n", verbosity=1, stdout=out)
    out.seek(0)
    lines = [line.strip() for line in out.readlines()]

    assert len(lines) == len(settings.LANGUAGES)
    for locale, _ in settings.LANGUAGES:
        assert "processing language %s" % locale in lines


LOCALIZED_CONTENT = {
    "en": "django",
    "fr": '"Hello world!": "Bonjour \\u00e0 tous !"',
    "zh_Hans": '"Hello world!": "\\u5927\\u5bb6\\u597d\\uff01"',
    "ko_KR": '"Hello world!": "\\uc548\\ub155\\ud558\\uc138\\uc694!"',
}


@pytest.mark.usefixtures("cleandir")
@pytest.mark.parametrize("locale", LOCALES)
def test_compile(settings, locale):
    out = io.StringIO()
    management.call_command("compilejsi18n", verbosity=1, stdout=out, locale=locale)
    out.seek(0)
    lines = [line.strip() for line in out.readlines()]

    assert len(lines) == 1
    assert lines[0] == "processing language %s" % locale
    basename = default_filename(locale, settings.STATICI18N_DOMAIN)
    filename = os.path.join(settings.STATICI18N_ROOT, "jsi18n", basename)
    assert os.path.exists(filename)
    with io.open(filename, "r", encoding="utf-8") as fp:
        content = fp.read()
        assert LOCALIZED_CONTENT[locale] in content


@pytest.mark.parametrize("locale", LOCALES)
def test_compile_no_use_i18n(settings, locale):
    """Tests compilation when `USE_I18N = False`.

    In this scenario, only the `settings.LANGUAGE_CODE` locale is processed
    (it defaults to `en-us` for Django projects).
    """
    settings.USE_I18N = False

    out = io.StringIO()
    management.call_command("compilejsi18n", verbosity=1, stdout=out, locale=locale)
    out.seek(0)
    lines = [line.strip() for line in out.readlines()]
    assert len(lines) == 1
    assert lines[0] == "processing language %s" % locale
    basename = default_filename(settings.LANGUAGE_CODE, settings.STATICI18N_DOMAIN)
    assert os.path.exists(os.path.join(settings.STATIC_ROOT, "jsi18n", basename))


@pytest.mark.parametrize("locale", ["en"])
@pytest.mark.parametrize("output_format", ["js", "json"])
def test_compile_with_output_format(settings, locale, output_format):
    out = io.StringIO()
    management.call_command(
        "compilejsi18n",
        verbosity=1,
        stdout=out,
        locale=locale,
        outputformat=output_format,
    )
    out.seek(0)
    lines = [line.strip() for line in out.readlines()]
    assert len(lines) == 1
    assert lines[0] == "processing language %s" % locale
    basename = default_filename(locale, settings.STATICI18N_DOMAIN, output_format)
    assert os.path.exists(os.path.join(settings.STATIC_ROOT, "jsi18n", basename))


@pytest.mark.parametrize("locale", ["en"])
@pytest.mark.parametrize("namespace", ["MyBlock"])
def test_compile_with_namespace(settings, locale, namespace):
    out = io.StringIO()
    management.call_command(
        "compilejsi18n",
        verbosity=1,
        stdout=out,
        locale=locale,
        outputformat="js",
        namespace=namespace,
    )
    out.seek(0)
    lines = [line.strip() for line in out.readlines()]
    assert len(lines) == 1
    assert lines[0] == "processing language %s" % locale
    basename = default_filename(locale, settings.STATICI18N_DOMAIN, "js")
    filename = os.path.join(settings.STATIC_ROOT, "jsi18n", basename)
    assert os.path.exists(filename)
    generated_content = open(filename).read()
    assert "global.MyBlock = MyBlock;" in generated_content


@pytest.mark.usefixtures("cleandir")
def test_compile_locale_not_exists():
    out = io.StringIO()
    management.call_command("compilejsi18n", locale="ar", verbosity=1, stderr=out)
    assert out.getvalue() == ""


@pytest.mark.parametrize("language", LANGUAGES)
def test_statici18n_templatetag(language):
    template = """
    {% load statici18n %}
    <script src="{% statici18n LANGUAGE_CODE %}"></script>
    """
    template = get_template_from_string(template)
    txt = template.render(Context({"LANGUAGE_CODE": language})).strip()
    assert txt == '<script src="/static/jsi18n/%s/djangojs.js"></script>' % language


@pytest.mark.usefixtures("cleandir")
@pytest.mark.parametrize("language", LANGUAGES)
def test_inlinei18n_templatetag(language):
    template = """
    {% load statici18n %}
    <script>{% inlinei18n LANGUAGE_CODE %}</script>
    """
    management.call_command("compilejsi18n")
    template = get_template_from_string(template)
    rendered = template.render(Context({"LANGUAGE_CODE": language})).strip()
    assert "django = globals.django || (globals.django = {});" in rendered
    assert "&quot;" not in rendered
    assert re.match("^<script>(r|b)'", rendered) is None
