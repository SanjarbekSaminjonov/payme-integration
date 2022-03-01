from django.urls import path
from .views import TestView


urlpatterns = [
    path('payme/', TestView.as_view()),
]
