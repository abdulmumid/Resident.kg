from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


def image_preview(obj):
    if obj.image:
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;" />')
    return 'Нет изображения'
image_preview.short_description = 'Изображение'


@admin.register(Popular)
class PopularAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'title', 'url', 'image_preview', 'created_at')
    readonly_fields = ('image_preview',)


@admin.register(CategoryRealEstate)
class CategoryRealEstateAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'category', 'created_at')


@admin.register(RealEstate)
class RealEstateAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'category', 'image_preview', 'title', 'created_at')
    readonly_fields = ('image_preview',)


@admin.register(CategoryLuxuryHoliday)
class CategoryLuxuryHolidayAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'category', 'created_at')


@admin.register(LuxuryHoliday)
class LuxuryHolidayAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'category', 'image_preview', 'title', 'created_at')
    readonly_fields = ('image_preview',)


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'title', 'author', 'studio', 'image_preview', 'created_at')
    readonly_fields = ('image_preview',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'title', 'image_preview', 'created_at')
    readonly_fields = ('image_preview',)


@admin.register(CompanyOffer)
class CompanyOfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'title', 'is_active', 'image_preview', 'created_at')
    readonly_fields = ('image_preview',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'title', 'image_preview', 'created_at')
    readonly_fields = ('image_preview',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'name', 'created_at')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'title', 'image_preview', 'created_at')
    readonly_fields = ('image_preview',)


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'short_text', 'image_preview', 'created_at')
    readonly_fields = ('image_preview',)

    def short_text(self, obj):
        return obj.text[:50] + '...'
    short_text.short_description = 'Текст'


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'title', 'order', 'image_preview', 'created_at')
    readonly_fields = ('image_preview',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'language', 'address', 'work_time',
        'journal_email', 'index', 'image_preview', 'created_at'
    )
    readonly_fields = ('image_preview',)
