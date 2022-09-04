from django.db import models
from django.core.validators import MinLengthValidator

class Breed(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2, "Название породы должно быть минимум из двух символов")]
    )

    def __str__(self):
        return self.name


class Cat(models.Model):
    nickname = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2, "Имя кошарика должно быть минимум из двух символов")]
    )
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=300)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
