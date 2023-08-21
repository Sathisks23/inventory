from django.db import models

class Product(models.Model):
    product_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    # Add other product fields as needed

    def __str__(self):
        return self.name


class Location(models.Model):
    location_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    # Add other location fields as needed

    def __str__(self):
        return self.name


class ProductMovement(models.Model):
    movement_id = models.CharField(primary_key=True, max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    from_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name='from_movements')
    to_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name='to_movements')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()

    def __str__(self):
        return self.movement_id

