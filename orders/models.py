from django.db import models


class Order(models.Model):
    client_name = models.CharField(max_length=100)
    amount = models.IntegerField()

