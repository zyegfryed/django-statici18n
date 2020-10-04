# import os
# import sys
import shutil
import pytest


# FIXME: wait for #216 to be merged
# See: https://github.com/pytest-dev/pytest-django/pull/216
# def pytest_configure():
#    BASE_DIR = os.path.join(os.path.dirname(__file__))
#    sys.path.append(os.path.realpath(os.path.join(BASE_DIR, "test_project")))
#    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


@pytest.fixture
def cleandir(request, settings):
    def teardown():
        shutil.rmtree(settings.STATICI18N_ROOT)

    request.addfinalizer(teardown)
