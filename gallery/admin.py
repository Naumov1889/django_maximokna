from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from .models import Video, VideoProperty, Photo, PhotoCategory


class VideoPropertyInline(SortableInlineAdminMixin, admin.TabularInline):  # or admin.StackedInline
    model = VideoProperty


@admin.register(Video)
class VideoPropertyAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = (VideoPropertyInline,)


class PhotoInline(SortableInlineAdminMixin, admin.TabularInline):  # or admin.StackedInline
    model = Photo


@admin.register(PhotoCategory)
class PhotoAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = (PhotoInline,)
