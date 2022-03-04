from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import Order
from .serializers import OrderSerializer

# Create your views here.


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
