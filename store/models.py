from django.db import models


class Marka(models.Model):
    marka_name = models.CharField(max_length=32)

    def __str__(self):
        return self.marka_name


class CarModel(models.Model):
    car_model = models.CharField(max_length=32)
    car_marka = models.ForeignKey(Marka, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_model


class Car(models.Model):
    car2_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=True, blank=True)
    car_name = models.CharField(max_length=32)
    description = models.TextField()
    year = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=32, null=True, blank=True)
    volume = models.FloatField(default=0, null=True, blank=True)
    carmarka = models.ForeignKey(Marka, on_delete=models.CASCADE, null=True, blank=True)

class CarPhoto(models.Model):
    car_image = models.ImageField(upload_to='img/', null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
