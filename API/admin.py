from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

# Базовый метод для превью изображений
def image_preview(obj):
    if obj.image:
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 100px;" />')
    return 'Нет изображения'
image_preview.short_description = 'Изображение'


@admin.register(Popular)
class PopularAdmin(admin.ModelAdmin):
    icon_name = "fire"  # 🔥 Популярное
    list_display = ('id', 'image_preview', 'created_at')
    # readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Category_Real_Estate)
class CategoryRealEstateAdmin(admin.ModelAdmin):
    icon_name = "home"  # 🏠 Недвижимость
    list_display = ('id', 'category', 'created_at')


@admin.register(Real_Estate)
class RealEstateAdmin(admin.ModelAdmin):
    icon_name = "home"  # 🏠 Недвижимость
    list_display = ('id', 'category', 'image_preview', 'title', 'time', 'created_at')
    # readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Category_Luxury_Holiday)
class CategoryLuxuryHolidayAdmin(admin.ModelAdmin):
    icon_name = "umbrella-beach"  # 🏖 Роскошные отпуска
    list_display = ('id', 'category', 'created_at')



@admin.register(Luxury_Holiday)
class LuxuryHolidayAdmin(admin.ModelAdmin):
    icon_name = "umbrella-beach"  # 🏖 Роскошные отпуска
    list_display = ('id', 'category', 'image_preview', 'title', 'created_at')
    # readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    icon_name = "microphone"  # 🎤 Интервью
    list_display = ('id', 'title', 'autor', 'studio', 'image_preview', 'created_at')
    # readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    icon_name = "box"  # 📦 Продукты
    list_display = ('id', 'title', 'image_preview', 'created_at')
    # readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(CompanyOffer)
class CompanyOfferAdmin(admin.ModelAdmin):
    icon_name = "tags"  # 🏷 Предложения
    list_display = ('id', 'title', 'url', 'is_active', 'image_preview', 'created_at')
    list_filter = ('is_active',)
    # readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    icon_name = "newspaper"  # 📰 Статьи
    list_display = ('id', 'title', 'image_preview', 'created_at')
    # readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    icon_name = "comments"  # 💬 Отзывы
    list_display = ('id', 'name', 'object_id', 'created_at')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    icon_name = "info-circle"  # ℹ️ О нас
    list_display = ('id', 'title', 'image_preview', 'created_at')
    # readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(About_Company)
class AboutCompanyAdmin(admin.ModelAdmin):
    icon_name = "building"  # 🏢 О компании
    list_display = ('id', 'created_at', 'short_text', 'image_preview')
    # readonly_fields = ('image_preview',)
    def short_text(self, obj): return obj.text[:50] + '...'
    short_text.short_description = 'Текст'
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    icon_name = "star"  # ⭐ Преимущества
    list_display = ('id', 'title', 'order', 'image_preview', 'created_at')
    # readonly_fields = ('image_preview',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    icon_name = "address-card"  # 📇 Контакт
    list_display = (
        'id', 'address', 'work_time', 'journal_email',
        'index','image_preview', 'created_at'
    )
    def image_preview(self, obj): return image_preview(obj)
