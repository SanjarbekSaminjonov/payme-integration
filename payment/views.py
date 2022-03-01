from paycomuz.views import MerchantAPIView
from paycomuz import Paycom


class CheckOrder(Paycom):
    def check_order(self, amount, account, **kwargs):
        return self.ORDER_FOUND


def successfully_payment(self, account, transaction, *args, **kwargs):
    print(account)


def cancel_payment(self, account, transaction, *args, **kwargs):
    print(account)


class TestView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder
