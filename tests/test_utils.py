import pytest

from statici18n import utils


@pytest.mark.parametrize("locale", ["en", "zh-hans", "ko-KR"])
def test_default_filename(locale):
    filename = utils.get_filename(locale, "djangojs")
    assert filename == "%s/djangojs.js" % locale


@pytest.mark.parametrize("fmt", ["js", "json", "yaml"])
def test_default_filename_with_outputformat(fmt):
    filename = utils.get_filename("en", "djangojs", fmt)
    assert filename == "en/djangojs.%s" % fmt


def test_legacy_filename(settings):
    settings.STATICI18N_FILENAME_FUNCTION = "statici18n.utils.legacy_filename"

    filename = utils.get_filename("en_GB", "djangojs")
    assert filename == "en-gb/djangojs.js"

    filename = utils.get_filename("zh-Hans", "djangojs")
    assert filename == "zh-hans/djangojs.js"


def custom_func(locale, domain):
    return "{0}-{1}.js".format(locale, domain)


def test_filename_with_custom_func(settings):
    settings.STATICI18N_FILENAME_FUNCTION = ".".join([__name__, "custom_func"])

    filename = utils.get_filename("es", "djangojs")
    assert filename == "es-djangojs.js"


def test_filename_with_no_func(settings):
    settings.STATICI18N_FILENAME_FUNCTION = "no_func"

    with pytest.raises(ImportError):
        utils.get_filename("es", "djangojs")


@pytest.mark.parametrize(
    "packages", ["mypackage1+mypackage2", ["mypackage1", "mypackage2"]]
)
def test_get_packages(packages):
    assert utils.get_packages(packages) == "mypackage1+mypackage2"


def test_get_packages_None():
    assert utils.get_packages("django.conf") is None
