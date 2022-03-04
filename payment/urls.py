from django.urls import path
from .views import PaymentView, checkout_view


urlpatterns = [
    path('payme/', PaymentView.as_view()),
    path('checkout/', checkout_view),
]
