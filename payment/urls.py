from django.urls import path
from .views import PaymentView


urlpatterns = [
    path('payme/', PaymentView.as_view()),
]
