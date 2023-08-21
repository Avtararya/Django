from django.db import models

INVOICE_FORMAT_CHOICES = (
    (1, 'Format 1'),
    (2, 'Format 2'),
    # Add more formats as needed
)

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=200)
    invoice_format = models.PositiveSmallIntegerField(choices=INVOICE_FORMAT_CHOICES)

    def __str__(self):
        return f"Invoice {self.invoice_number}"
