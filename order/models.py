from django.db import models

# Create your models here.


class Order(models.Model):
    is_payed = models.BooleanField(default=False, blank=True, null=True)
    amount = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    amount_for_payme = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    number_of_people = models.IntegerField(default=1, blank=True, null=True)
    place_id = models.IntegerField(blank=True, null=True)
    place_name = models.CharField(max_length=1000, blank=True, null=True)
    customer_full_name = models.CharField(max_length=255, blank=True, null=True)
    customer_passport = models.CharField(max_length=255, blank=True, null=True)
    customer_phone_number = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} - {self.amount} - {self.customer_full_name} {self.customer_phone_number}"

    def save(self, *args, **kwargs):
        self.amount_for_payme = self.amount * 100
        super(Order, self).save(*args, **kwargs)

