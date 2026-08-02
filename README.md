# django-statici18n

A Django app that compiles i18n JavaScript catalogs to static files.

## Installation

Install the package via pip:

```bash
pip install django-statici18n
```

Add it to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "statici18n",
]
```

## Configuration

Configure the following settings in your `settings.py` (optional defaults shown):

```python
STATICI18N_DOMAIN = "djangojs"
STATICI18N_PACKAGES = "django.conf"
STATICI18N_ROOT = STATIC_ROOT
STATICI18N_OUTPUT_DIR = "jsi18n"
STATICI18N_FILENAME_FUNCTION = "statici18n.utils.default_filename"
STATICI18N_NAMESPACE = None
```

## Usage

### Compile JavaScript Catalogs

Run the management command to generate static i18n catalogs:

```bash
python manage.py compilejsi18n
```

Available options:

- `--locale`, `-l`: Process specific locale(s)
- `--domain`, `-d`: Override gettext domain (default: `djangojs`)
- `--packages`, `-p`: Specify translation packages
- `--output`, `-o`: Set output directory (default: `jsi18n` in `STATIC_ROOT`)
- `--format`, `-f`: Output format (`js` or `json`, default: `js`)
- `--namespace`, `-n`: Set JavaScript namespace

Example:

```bash
python manage.py compilejsi18n -l en -l fr -o static/jsi18n/
```

### Template Tags

Use these template tags to reference compiled catalogs:

**`{% statici18n locale %}`**: Returns URL to JavaScript catalog for the given locale.

**`{% inlinei18n locale %}`**: Inlines the catalog content directly in a `<script>` block.

Example templates:

```django
{% load statici18n %}
<script src="{% statici18n 'fr' %}"></script>

<script>{% inlinei18n 'fr' %}</script>
```

## Testing

Run tests using pytest:

```bash
tox
```

Or with coverage:

```bash
tox -e coverage
```

## Documentation

Documentation is available on [Read the Docs](http://django-statici18n.readthedocs.org/)

## License

BSD License
