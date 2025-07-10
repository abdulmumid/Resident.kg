from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from .forms import BasePhoneForm

def image_preview(obj):
    if hasattr(obj, 'image') and obj.image:
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 100px;" />')
    return 'Нет изображения'
image_preview.short_description = 'Изображение'


@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    form = BasePhoneForm
    icon_name = "person"  
    list_display = ('id', 'name', 'email', 'phone', 'created_at', 'updated_at') 
    search_fields = ('name', 'first_name', 'email')


@admin.register(Popular)
class PopularAdmin(admin.ModelAdmin):
    icon_name = "whatshot"  # огонь
    list_display = ('slug', 'title', 'url', 'image_preview', 'created_at')
    search_fields = ('title', 'slug')
    def image_preview(self, obj): return image_preview(obj)


@admin.register(CategoryRealEstate)
class CategoryRealEstateAdmin(admin.ModelAdmin):
    icon_name = "home"
    list_display = ('category', 'created_at')
    search_fields = ('category',)


@admin.register(RealEstate)
class RealEstateAdmin(admin.ModelAdmin):
    icon_name = "home"
    list_display = ('slug', 'category', 'image_preview', 'title', 'created_at')
    search_fields = ('title', 'slug')
    def image_preview(self, obj): return image_preview(obj)


@admin.register(CategoryLuxuryHoliday)
class CategoryLuxuryHolidayAdmin(admin.ModelAdmin):
    icon_name = "beach_access"
    list_display = ('category', 'created_at')
    search_fields = ('category',)


@admin.register(LuxuryHoliday)
class LuxuryHolidayAdmin(admin.ModelAdmin):
    icon_name = "beach_access"
    list_display = ('slug', 'category', 'image_preview', 'title', 'created_at')
    search_fields = ('title', 'slug')
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    icon_name = "mic"
    list_display = ('title', 'author', 'studio', 'image_preview', 'created_at')
    search_fields = ('title', 'author')
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    icon_name = "inventory_2"  # коробка
    list_display = ('slug', 'title', 'image_preview', 'created_at')
    search_fields = ('title', 'slug')
    def image_preview(self, obj): return image_preview(obj)


@admin.register(CompanyOffer)
class CompanyOfferAdmin(admin.ModelAdmin):
    icon_name = "label"
    list_display = ('title', 'url', 'is_active', 'image_preview', 'created_at')
    search_fields = ('title',)
    list_filter = ('is_active',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    icon_name = "article"
    list_display = ('slug', 'title', 'image_preview', 'created_at')
    search_fields = ('title', 'slug')
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    icon_name = "chat_bubble"
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    icon_name = "info"
    list_display = ('title', 'image_preview', 'created_at')
    search_fields = ('title',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    icon_name = "apartment"
    list_display = ('id', 'created_at', 'short_text', 'image_preview')
    readonly_fields = ('image_preview',)
    def short_text(self, obj): return obj.text[:50] + '...'
    short_text.short_description = 'Текст'
    def image_preview(self, obj): return image_preview(obj)


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    icon_name = "star"
    list_display = ('title', 'order', 'image_preview', 'created_at')
    search_fields = ('title',)
    def image_preview(self, obj): return image_preview(obj)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    icon_name = "contacts"
    list_display = (
        'id', 'address', 'work_time', 'journal_email',
        'index', 'image_preview', 'created_at'
    )
    search_fields = ('address', 'journal_email')
    def image_preview(self, obj): return image_preview(obj)
