from django.contrib import admin
from django.template.defaultfilters import truncatechars
from adminsortable2.admin import SortableAdminMixin
from .models import Social

@admin.register(Social)
class SocialAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('short_link', 'icon', 'icon_larger')
    list_display_links = ('short_link',)
    list_editable = ('icon', 'icon_larger')

    def short_link(self, obj):
        return truncatechars(obj.link, 30)
