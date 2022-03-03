from paycomuz.views import MerchantAPIView
from paycomuz import Paycom
from order.models import Order


class CheckOrder(Paycom):
    def check_order(self, amount, account, **kwargs):
        order_id = int(account['order_id'])
        order = Order.objects.filter(id=order_id).first()
        if order is not None:
            if str(amount) != order.amount:
                return self.INVALID_AMOUNT
            return self.ORDER_FOUND
        else:
            return self.ORDER_NOT_FOND

    def successfully_payment(self, account, transaction, *args, **kwargs):
        order_id = int(transaction.order_key)
        order = Order.objects.filter(id=order_id).first()
        order.is_payed = True
        order.save()

    def cancel_payment(self, account, transaction, *args, **kwargs):
        order_id = int(transaction.order_key)
        order = Order.objects.filter(id=order_id).first()
        order.is_payed = False
        order.save()


class TestView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder
