from django.db import models
from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = AutoSlugField(populate_from="title", always_update="True", unique="True", db_index=True, max_length=220)
    subtitle = models.CharField(max_length=200, verbose_name="Подзаголовок")
    img_square = models.ImageField(default="blog_default_square.jpg", verbose_name="Квадратная картинка")
    img_long = models.ImageField(default="blog_default_long.jpg", verbose_name="Широкая картинка")
    text = RichTextUploadingField(default="<div class='container'>      </div>", verbose_name="Текст")
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']

        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" style="max-width:200px;max-height:150px" />' % (self.img_square))

    image_tag.short_description = 'Превью'
    image_tag.allow_tags = True

    def __str__(self):
        return self.title
