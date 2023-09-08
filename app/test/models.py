from django.db import models

class Customer(models.Model):
    GENRE_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    customer_id = models.PositiveIntegerField(primary_key=True)
    genre = models.CharField(max_length=6, choices=GENRE_CHOICES)
    age = models.PositiveIntegerField()
    annual_income = models.PositiveIntegerField()
    spending_score = models.PositiveIntegerField()

