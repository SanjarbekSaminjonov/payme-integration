from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import Order
from .serializers import OrderCreateSerializer, OrderViewSerializer

# Create your views here.


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer


class OrderDetailAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderViewSerializer
