from django.db import models


class Banner(models.Model):
    link = models.CharField(max_length=200, default=None, blank=True, null=True, verbose_name="Ссылка")
    desktop = models.ImageField(default=None, verbose_name="Большие экраны (от 750px)")
    tablet = models.ImageField(default=None, verbose_name="Планшеты (от 600px до 750px)")
    mobile = models.ImageField(default=None, verbose_name="Телефоны (до 600px)")
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']

        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" style="max-width:200px;max-height:150px" />' % (self.desktop))

    image_tag.short_description = 'Превью'
    image_tag.allow_tags = True


class PortfolioCategory(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    text = models.TextField(max_length=260, default="", verbose_name="Текст")
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']
        verbose_name = "Галерея с фото работ"
        verbose_name_plural = "Галереи с фото работ"

    def __str__(self):
        return self.title


class PortfolioPhoto(models.Model):
    picture_top = models.ImageField(default=None, verbose_name="Верхняя")
    picture_bottom = models.ImageField(blank=True, null=True, verbose_name="Нижняя")
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.picture_top.url

    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']
        verbose_name = "Фото работ"
        verbose_name_plural = "Фото работ"


class Advantage(models.Model):
    title = models.CharField(max_length=40, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    picture = models.ImageField(default=None, verbose_name="Картинка")

    def __str__(self):
        return self.title

    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name="Сортировать")

    class Meta(object):
        ordering = ['order']
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" style="max-width:200px;max-height:150px" />' % (self.picture))

    image_tag.short_description = 'Превью'
    image_tag.allow_tags = True


class FirstScreenImg(models.Model):
    tablet = models.ImageField(default="bg-first-screen.jpg", verbose_name="Для планшета (от 500px до 1250px)")
    mobile = models.ImageField(default="bg-first-screen-mobile.jpg", verbose_name="Для мобильных (до 500px)")
    isDark = models.BooleanField(default=False, verbose_name="Темный бургер и НАШИ РАБОТЫ")

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" style="max-width:200px;max-height:150px" />' % (self.mobile))

    image_tag.short_description = 'Превью'
    image_tag.allow_tags = True


    def __str__(self):
        return self.mobile.url

    class Meta(object):
        verbose_name = "Картинка для первого экрана главной страницы"
        verbose_name_plural = "Картинка для первого экрана главной страницы"
