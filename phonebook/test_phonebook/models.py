from django.db import models

class Peeps(models.Model):
    phone_number = models.CharField("Номер телефона", max_length=11)
    last_name = models.CharField("Фамилия", max_length=20)
    first_name = models.ForeignKey("names", on_delete=models.SET_NULL, null=True)
    middle_name = models.ForeignKey("patronymic", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Фамилия"
        verbose_name_plural = "Фамилии"

    def __str__(self):
        return self.last_name

class Names(models.Model):
    first_name = models.CharField("Имя", max_length=20)
    
    class Meta:
        verbose_name = "Имя"
        verbose_name_plural = "Имена"

    def __str__(self):
        return self.first_name

class Patronymic(models.Model):
    middle_name = models.CharField("Отчетсво", max_length=20)

    class Meta:
        verbose_name = "Отчетсво"
        verbose_name_plural = "Отчества"

    def __str__(self):
        return self.middle_name