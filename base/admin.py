from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from .models import Banner, PortfolioCategory, PortfolioPhoto, Advantage, FirstScreenImg


@admin.register(Banner)
class BannerAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('image_tag', 'link', 'desktop', 'tablet', 'mobile')
    list_display_links = ('image_tag',)
    list_editable = ('link', 'desktop', 'tablet', 'mobile')
    # fields = ['image_tag']
    readonly_fields = ['image_tag']


class PortfolioPhotoInline(SortableInlineAdminMixin, admin.TabularInline):  # or admin.StackedInline
    model = PortfolioPhoto


@admin.register(PortfolioCategory)
class PortfolioPhotoAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = (PortfolioPhotoInline,)


@admin.register(Advantage)
class AdvantageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'text', 'picture')
    list_display_links = ('image_tag',)
    list_editable = ('title', 'text', 'picture')
    readonly_fields = ['image_tag']


class FirstScreenImgAdmin(admin.ModelAdmin):
    list_display = ('tablet', 'mobile', 'isDark', 'image_tag')
    list_display_links = ('image_tag',)
    list_editable = ('tablet', 'mobile', 'isDark')
    readonly_fields = ['image_tag']


admin.site.register(FirstScreenImg, FirstScreenImgAdmin)
