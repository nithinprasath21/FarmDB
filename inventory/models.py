from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

class Transporter(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    vehicle_number = models.CharField(max_length=20)

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    quantity = models.IntegerField()
    storage_area = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
