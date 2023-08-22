from django.db import models

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)
    invoice_format = models.IntegerField()

    def __str__(self):
        return self.invoice_number
