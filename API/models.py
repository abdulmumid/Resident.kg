from django.db import models
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from phonenumber_field.modelfields import PhoneNumberField
from API.choices import LANGUAGE_CHOICES  
from django.contrib.auth.hashers import make_password



# Регистрация Пользователя
class UserRegistration(models.Model):
    language = models.CharField(('Язык'), max_length=10, choices=LANGUAGE_CHOICES)
    name = models.CharField(('ФИО'), max_length=20)
    phone = PhoneNumberField('Телефон')
    email = models.EmailField('Email', unique=True)
    password = models.CharField('Пароль', max_length=128)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.pk or not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Регистрация Пользователя'
        verbose_name_plural = 'Регистрации Пользователей'
        ordering = ['-id']



# Модель для популярного контента
class Popular(models.Model):
    language = models.CharField(('Язык'), max_length=10, choices=LANGUAGE_CHOICES) 
    title = models.CharField('Заголовок', max_length=30)  
    text = RichTextUploadingField('Текст')  
    url = models.URLField('URL', blank=True)  
    image = models.ImageField('Изображение', upload_to='popular_images/') 
    slug = models.SlugField('Слаг', max_length=255, unique=True, null=True, blank=True) 
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)  
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)  

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Популярное'
        verbose_name_plural = 'Популярные'
        ordering = ['-created_at']  


# Категория для недвижимости
class CategoryRealEstate(models.Model):
    category = models.CharField('Категория', max_length=50)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория - Недвижимость'
        verbose_name_plural = 'Категории - Недвижимость'
        ordering = ['-created_at']


# Основная модель для недвижимости
class RealEstate(models.Model):
    language = models.CharField(('Язык'), max_length=10, choices=LANGUAGE_CHOICES)
    category = models.ForeignKey(CategoryRealEstate, on_delete=models.CASCADE, related_name='real_estates', verbose_name='Категория')
    image = models.ImageField('Изображение', upload_to='real_estate_images/')
    title = models.CharField('Название', max_length=255)
    text = RichTextUploadingField('Текст', blank=True, null=True)
    slug = models.SlugField('Слаг', max_length=255, unique=True, null=True, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'
        ordering = ['-created_at']


# Категория для роскошного отдыха
class CategoryLuxuryHoliday(models.Model):
    category = models.CharField('Категория', max_length=50)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория - Роскошный отдых'
        verbose_name_plural = 'Категории - Роскошного отдыха'
        ordering = ['-created_at']


# Модель для роскошного отдыха
class LuxuryHoliday(models.Model):
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    category = models.ForeignKey(CategoryLuxuryHoliday, on_delete=models.CASCADE, related_name='luxury_holidays', verbose_name='Категория')
    image = models.ImageField('Изображение', upload_to='luxury_holiday_images/')
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField('Слаг', max_length=255, unique=True, null=True, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Роскошный отдых'
        verbose_name_plural = 'Роскошный отдых'
        ordering = ['-created_at']


# Интервью
class Interview(models.Model):
    language = models.CharField(('Язык'), max_length=10, choices=LANGUAGE_CHOICES)
    title = models.CharField('Заголовок', max_length=255)
    author = models.CharField('Автор', max_length=255)
    studio = models.CharField('Студия', max_length=255)
    image = models.ImageField('Изображение', upload_to='interview_images/')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Интервью'
        verbose_name_plural = 'Интервью'
        ordering = ['-created_at']


# Продукты
class Product(models.Model):
    language = models.CharField(('Язык'), max_length=10, choices=LANGUAGE_CHOICES)
    title = models.CharField('Заголовок', max_length=255)
    text = RichTextUploadingField('Текст')
    image = models.ImageField('Изображение', upload_to='product_images/')
    slug = models.SlugField('Слаг', max_length=255, unique=True, null=True, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-created_at']


# Предложения от компаний
class CompanyOffer(models.Model):
    language = models.CharField(('Язык'), max_length=10, choices=LANGUAGE_CHOICES)
    title = models.CharField('Заголовок', max_length=255)
    image = models.ImageField('Изображение', upload_to='company_offer_images/')
    url = models.URLField('URL', blank=True, null=True)
    is_active = models.BooleanField('Активен', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Предложение от компании'
        verbose_name_plural = 'Предложения от компании'
        ordering = ['-created_at']


# Статьи
class Article(models.Model):
    language = models.CharField(('Язык'), max_length=10, choices=LANGUAGE_CHOICES)
    title = models.CharField('Заголовок', max_length=255)
    text = RichTextUploadingField('Текст')
    image = models.ImageField('Изображение', upload_to='article_images/')
    slug = models.SlugField('Слаг', max_length=255, unique=True, null=True, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


# Отзывы
class Review(models.Model):
    language = models.CharField(('Язык'), max_length=10, choices=LANGUAGE_CHOICES)
    name = models.CharField('Имя', max_length=30)
    review = RichTextUploadingField('Отзыв')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']


# О нас (короткая информация)
class About(models.Model):
    language = models.CharField(('Язык'), max_length=10, choices=LANGUAGE_CHOICES)
    title = models.CharField('Заголовок', max_length=255)
    image = models.ImageField('Изображение', upload_to='about_images/')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        ordering = ['-created_at']


# О компании (более детально)
class AboutCompany(models.Model):
    language = models.CharField(('Язык'), max_length=10, choices=LANGUAGE_CHOICES)
    text = RichTextUploadingField('О Компании')
    image = models.ImageField('Изображение', upload_to='about_company_images/')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.text[:50] + '...'

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'
        ordering = ['-created_at']


# Преимущества
class Advantage(models.Model):
    language = models.CharField(('Язык'), max_length=10, choices=LANGUAGE_CHOICES)
    title = models.CharField('Заголовок', max_length=255)
    icon = models.ImageField('Иконка', upload_to='advantage_icons/', blank=True, null=True)
    order = models.PositiveIntegerField('Порядок', default=0)  # Используется для сортировки
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
        ordering = ['order', '-created_at']


# Контактная информация
class ContactInfo(models.Model):
    language = models.CharField(('Язык'), max_length=10, choices=LANGUAGE_CHOICES)
    address = models.CharField('Адрес', max_length=255)
    work_time = models.CharField('Время работы', max_length=100)
    journal_email = models.EmailField('Email (Журнал)')
    pr_email = models.EmailField('Email (PR)')
    hr_email = models.EmailField('Email (HR)')
    index = models.CharField('Индекс', max_length=10, blank=True)
    license_number = models.CharField('Лицензия', max_length=20, blank=True)
    registration_code = models.CharField('Регистрационный код', max_length=20, blank=True)
    facebook_link = models.URLField('Facebook', blank=True)
    instagram_link = models.URLField('Instagram', blank=True)
    tiktok_link = models.URLField('TikTok', blank=True)
    image = models.ImageField('Изображение', upload_to='contact_info_images/')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return "Контактная информация"

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'
        ordering = ['-created_at']
