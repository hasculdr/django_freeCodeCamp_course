from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(("Manufacturer"), max_length=50)

    def __str__(self):
        return self.name

class Auto(models.Model):
    nickname = models.CharField(("Nickname"), max_length=20)
    mileage = models.IntegerField(("Milleage"), default=0)
    comments = models.CharField(("Comments"), max_length=50)
    auto = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
