from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    "",
    path("", TemplateView.as_view(template_name="base.html")),
    path("jsi18n/", "django.views.i18n.javascript_catalog", name="jsi18n"),
]
