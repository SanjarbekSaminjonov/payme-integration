from django.db import models

# Create your models here.


class Order(models.Model):
    is_payed = models.BooleanField(default=False, blank=True, null=True)
    amount = models.CharField(max_length=255, blank=True, null=True)
    number_of_people = models.IntegerField(default=1, blank=True, null=True)
    place_id = models.CharField(max_length=255, blank=True, null=True)
    place_name = models.CharField(max_length=1000, blank=True, null=True)
    customer_full_name = models.CharField(max_length=255, blank=True, null=True)
    customer_passport = models.CharField(max_length=255, blank=True, null=True)
    customer_phone_number = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} - {self.amount} - {self.customer_full_name} {self.customer_phone_number}"
