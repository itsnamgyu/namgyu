from django.apps import apps
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "core/index.html"


class WorkView(TemplateView):
    template_name = "core/work.html"


class BlogView(TemplateView):
    template_name = "core/blog.html"
