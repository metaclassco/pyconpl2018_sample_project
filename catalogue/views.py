from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'sample_project/catalogue/main.html'


class ErrorView(TemplateView):
    template_name = 'sample_project/catalogue/error.html'
