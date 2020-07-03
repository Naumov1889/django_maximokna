from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Post

@admin.register(Post)
class PostAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_tag', )
    list_display_links = ('image_tag', 'title')
    readonly_fields = ['image_tag']
