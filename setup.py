from setuptools import setup, find_packages

setup(
    name="django-statici18n",
    version="2.8.0",
    author="Sebastien Fievet",
    author_email="_@sebastien-fievet.net",
    url="http://django-statici18n.readthedocs.org/",
    description=("A Django app that compiles i18n JavaScript catalogs "
                 "to static files."),
    long_description=open("README.rst").read(),
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Django>=4.2,<6.2",
        "django-appconf>=1.0",
    ],
    license="BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 5.2",
        "Framework :: Django :: 6.0",
        "Framework :: Django :: 6.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    project_urls={
        "Source": "https://github.com/zyegfryed/django-statici18n",
    },
)
