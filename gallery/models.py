from django.db import models
from autoslug import AutoSlugField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class Video(models.Model):
    title = models.CharField(max_length=100)
    videoId = models.CharField(max_length=20)

    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self):
        return self.title


class VideoProperty(models.Model):
    property = models.CharField(max_length=100, verbose_name="Свойство")
    description = models.CharField(max_length=100, verbose_name="Описание")
    video = models.ForeignKey(Video, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.property

    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']
        verbose_name = "Свойство"
        verbose_name_plural = "Свойства"


class PhotoCategory(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    slug = AutoSlugField(populate_from="title", always_update="True", unique="True", db_index=True, max_length=60)

    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']
        verbose_name = "Галерея с фото"
        verbose_name_plural = "Галерии с фото"

    def __str__(self):
        return self.title


class Photo(models.Model):
    caption = models.CharField(max_length=100, blank=True, verbose_name="Подпись")
    picture = models.ImageField(default=None, verbose_name="Фото")
    thumbnail = ImageSpecField(source='picture',
                               processors=[ResizeToFit(400, 400)],
                               format='JPEG',
                               options={'quality': 80})
    category = models.ForeignKey(PhotoCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']
        verbose_name = "Фото"
        verbose_name_plural = "Фото"
