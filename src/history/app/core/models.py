from django.db import models
class History(models.Model):
    product_id=models.PositiveIntegerField()
    customer_id=models.PositiveIntegerField()
    employee_id=models.PositiveIntegerField()
    price=models.FloatField()
