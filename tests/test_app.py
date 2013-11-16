import os
import pytest

from django.core import management
from django.template import loader, Context
from django.utils import six


@pytest.mark.usefixtures("cleandir")
def test_compile_all(settings):
    out = six.StringIO()
    management.call_command('compilejsi18n', verbosity=1, stdout=out)
    out.seek(0)
    lines = [l.strip() for l in out.readlines()]
    assert len(lines) == 2
    assert lines[0] == "processing language en"
    assert lines[1] == "processing language fr"
    filename = os.path.join(
        settings.STATICI18N_ROOT, "jsi18n", "fr", "djangojs.js")
    assert os.path.exists(filename)
    with open(filename) as fp:
        content = fp.read()
        assert "django.catalog" in content
        assert '"Hello world!": "Bonjour tout le monde !"' in content


@pytest.mark.usefixtures("cleandir")
def test_compile_locale_not_exists(settings):
    out = six.StringIO()
    management.call_command('compilejsi18n', locale='ar', verbosity=1, stderr=out)
    assert out.getvalue() == ""


def test_templatetag(settings):
    template = """
    {% load statici18n %}
    <script src="{% statici18n LANGUAGE_CODE %}"></script>
    """
    template = loader.get_template_from_string(template)
    assert template.render(Context({'LANGUAGE_CODE': 'fr'})).strip() ==\
        '<script src="/static/jsi18n/fr/djangojs.js"></script>'
