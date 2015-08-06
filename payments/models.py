from django.db import models

class Payment(models.Model):
    account = models.ForeignKey('accounts.IthacashAccount', related_name="payments")


class SignUpPayment(Payment):
    created = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    txn_id = models.CharField(max_length=255)

