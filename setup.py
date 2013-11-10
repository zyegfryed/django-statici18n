from setuptools import setup, find_packages

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name="django-statici18n",
    version=__import__('statici18n').__version__,
    description="A Django app that provides helper for generating "
                "Javascript catalog to static files.",
    long_description=long_description,
    author="Sebastien Fievet",
    author_email="zyegfryed@gmail.com",
    license="BSD",
    url="http://django-statici18n.readthedocs.org/",
    packages=find_packages(exclude=['tests']),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=False,
    install_requires=[
        'django-appconf>=0.4',
    ],
)
