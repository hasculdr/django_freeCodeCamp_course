from django.db import models

class Peeps(models.Model):
    phone_number = models.CharField("Номер телефона", max_length=11)
    last_name = models.CharField("Фамилия", max_length=20)
    first_name = models.ForeignKey("names", on_delete=models.SET_NULL, null=True)
    middle_name = models.ForeignKey("patronymics", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"""{self.last_name} {self.first_name} {self.middle_name} {self.phone_number}"""

class Names(models.Model):
    first_name = models.CharField("Имя", max_length=20)
    
    class Meta:
        verbose_name = "Имя"
        verbose_name_plural = "Имена"

    def __str__(self):
        return self.first_name

class Patronymics(models.Model):
    middle_name = models.CharField("Отчетсво", max_length=20)

    class Meta:
        verbose_name = "Отчетсво"
        verbose_name_plural = "Отчества"

    def __str__(self):
        return self.middle_name