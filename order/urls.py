from django.urls import path
from .views import OrderCreateAPIView, OrderDetailAPIView


urlpatterns = [
    path('create/', OrderCreateAPIView.as_view()),
    path('detail/<str:pk>/', OrderDetailAPIView.as_view())
]
