from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

def image_preview(obj):
    if hasattr(obj, 'image') and obj.image:
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 100px;" />')
    return 'Нет изображения'
image_preview.short_description = 'Изображение'


@admin.register(Popular)
class PopularAdmin(admin.ModelAdmin):
    icon_name = "🔥"
    list_display = ('slug', 'title', 'url', 'image_preview', 'created_at')
    search_fields = ('title', 'slug')
    readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(CategoryRealEstate)
class CategoryRealEstateAdmin(admin.ModelAdmin):
    icon_name = "🏠"
    list_display = ('category', 'created_at')
    search_fields = ('category',)


@admin.register(RealEstate)
class RealEstateAdmin(admin.ModelAdmin):
    icon_name = "🏠"
    list_display = ('slug', 'category', 'image_preview', 'title', 'created_at')
    search_fields = ('title', 'slug')
    readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(CategoryLuxuryHoliday)
class CategoryLuxuryHolidayAdmin(admin.ModelAdmin):
    icon_name = "🏖"
    list_display = ('category', 'created_at')
    search_fields = ('category',)


@admin.register(LuxuryHoliday)
class LuxuryHolidayAdmin(admin.ModelAdmin):
    icon_name = "🏖"
    list_display = ('slug', 'category', 'image_preview', 'title', 'created_at')
    search_fields = ('title', 'slug')
    readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    icon_name = "🎤"
    list_display = ('title', 'author', 'studio', 'image_preview', 'created_at')
    search_fields = ('title', 'author')
    readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    icon_name = "📦"
    list_display = ('slug', 'title', 'image_preview', 'created_at')
    search_fields = ('title', 'slug')
    readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(CompanyOffer)
class CompanyOfferAdmin(admin.ModelAdmin):
    icon_name = "🏷"
    list_display = ('title', 'url', 'is_active', 'image_preview', 'created_at')
    search_fields = ('title',)
    list_filter = ('is_active',)
    readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    icon_name = "📰"
    list_display = ('slug', 'title', 'image_preview', 'created_at')
    search_fields = ('title', 'slug')
    readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    icon_name = "💬"
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    icon_name = "ℹ️"
    list_display = ('title', 'image_preview', 'created_at')
    search_fields = ('title',)
    readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    icon_name = "🏢"
    list_display = ('id', 'created_at', 'short_text', 'image_preview')
    readonly_fields = ('image_preview',)
    def short_text(self, obj): return obj.text[:50] + '...'
    short_text.short_description = 'Текст'
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    icon_name = "⭐"
    list_display = ('title', 'order', 'image_preview', 'created_at')
    search_fields = ('title',)
    readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    icon_name = "📇"
    list_display = (
        'id', 'address', 'work_time', 'journal_email',
        'index', 'image_preview', 'created_at'
    )
    search_fields = ('address', 'journal_email')
    readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)