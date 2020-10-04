from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name="base.html")),
    url(r"^jsi18n/$", "django.views.i18n.javascript_catalog", name="jsi18n"),
)
