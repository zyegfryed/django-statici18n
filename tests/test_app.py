import io
import os
import pytest

from django.core import management
from django.template import Context
from django.utils import six

try:
    # Django >= 1.8
    from django.template import Engine

    def get_template_from_string(template_code):
        return Engine().from_string(template_code)

except ImportError:
    # Django < 1.8
    from django.template import loader

    get_template_from_string = loader.get_template_from_string


@pytest.mark.usefixtures("cleandir")
def test_compile_all(settings):
    out = six.StringIO()
    management.call_command('compilejsi18n', verbosity=1, stdout=out)
    out.seek(0)
    lines = [l.strip() for l in out.readlines()]
    assert len(lines) == 2
    assert lines[0] == "processing language en"
    assert lines[1] == "processing language fr"
    assert os.path.exists(os.path.join(
        settings.STATIC_ROOT, "jsi18n", "en", "djangojs.js"))
    filename = os.path.join(
        settings.STATICI18N_ROOT, "jsi18n", "fr", "djangojs.js")
    assert os.path.exists(filename)
    with io.open(filename, "r", encoding="utf-8") as fp:
        content = fp.read()
        assert "django.catalog" in content
        assert '"Hello world!": "Bonjour \\u00e0 tous !"' in content


@pytest.mark.usefixtures("cleandir")
def test_compile_locale_not_exists(settings):
    out = six.StringIO()
    management.call_command('compilejsi18n', locale='ar', verbosity=1, stderr=out)
    assert out.getvalue() == ""


def test_statici18n_templatetag(settings):
    template = """
    {% load statici18n %}
    <script src="{% statici18n LANGUAGE_CODE %}"></script>
    """
    template = get_template_from_string(template)
    assert template.render(Context({'LANGUAGE_CODE': 'fr'})).strip() ==\
        '<script src="/static/jsi18n/fr/djangojs.js"></script>'


@pytest.mark.usefixtures("cleandir")
def test_inlinei18n_templatetag(settings):
    template = """
    {% load statici18n %}
    <script src="{% inlinei18n LANGUAGE_CODE %}"></script>
    """
    management.call_command('compilejsi18n')
    template = get_template_from_string(template)
    rendered = template.render(Context({'LANGUAGE_CODE': 'fr'})).strip()
    assert 'var django = globals.django || (globals.django = {});' in rendered
