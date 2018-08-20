from django.urls import path

from .views import ErrorView, MainView


urlpatterns = [
    path('catalogue/', MainView.as_view(), name='catalogue'),
    path('catalogue/error', ErrorView.as_view(), name='catalogue_error'),
]
