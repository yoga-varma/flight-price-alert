from django.db import models
from django.contrib.auth.models import User

class Route(models.Model):
    origin = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.origin} → {self.destination}"


class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    target_price = models.FloatField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} - {self.route} - {self.target_price}"


class PriceSnapshot(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    price = models.FloatField()
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.route} - {self.price}"