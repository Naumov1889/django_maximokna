from django.db import models

class Callback(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    whenToCall = models.CharField(max_length=20, blank=True, verbose_name="Когда позвонить")
    email = models.CharField(max_length=40, blank=True, verbose_name="Почта")

    def __str__(self):
        return self.name

    class Meta(object):
        verbose_name = "Запрос на обратную связь"
        verbose_name_plural = "Запросы на обратную связь"
