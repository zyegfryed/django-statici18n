from setuptools import setup, find_packages

setup(
    name="django-statici18n",
    version="2.1.1",
    author="Sebastien Fievet",
    author_email="zyegfryed@gmail.com",
    url="http://django-statici18n.readthedocs.org/",
    description="A Django app that provides helper for generating "
    "Javascript catalog to static files.",
    long_description=open("README.rst").read(),
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Django>=2.2",
        "django-appconf>=1.0",
    ],
    license="BSD",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    project_urls={
        "Source": "https://github.com/zyegfryed/django-statici18n",
    },
)
