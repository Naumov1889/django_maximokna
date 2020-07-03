from django.db import models

class Social(models.Model):
    link = models.CharField(max_length=400)
    icon = models.TextField(default=None, verbose_name="Иконка")
    icon_larger = models.TextField(default=None, verbose_name="Иконка большего размера")
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']
        verbose_name = "Соцсеть"
        verbose_name_plural = "Соцсети"

    def __str__(self):
        return self.link
