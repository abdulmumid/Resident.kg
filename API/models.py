from django.db import models


# Популярные изображения
class Popular(models.Model):
    image = models.ImageField(('Изображение'), upload_to='popular_images/')
    created_at = models.DateTimeField(('Дата создания'), auto_now_add=True)

    def __str__(self):
        return f"Popular Image {self.id}"
    
    class Meta:
        verbose_name = 'Популярное'
        verbose_name_plural = 'Популярные'
        ordering = ['-id']  


#Категория-Недвижимость
class Category_Real_Estate(models.Model):
    category = models.CharField(('Категория'), max_length=20)
    created_at = models.DateTimeField(('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = 'Категория-Недвижомость'
        verbose_name_plural = 'Категории-Недвижимостей'
        ordering = ['-id']


# Недвижимость
class Real_Estate(models.Model):
    category = models.ForeignKey(Category_Real_Estate, on_delete=models.CASCADE, related_name='Real_Estate', verbose_name='Категория')
    image = models.ImageField(('Изображение'), upload_to='real_estate_images/')
    title = models.CharField(('Название'), max_length=255)
    text = models.TextField(('Текст'), blank=True, null=True)
    time = models.DateTimeField(('Время'), auto_now_add=True)
    created_at = models.DateTimeField(('Дата создания'), auto_now_add=True)

    def __str__(self):
        return f"Real Estate Image {self.id}"

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимости'
        ordering = ['-id']  


#Категория-Росскошный одддых
class Category_Luxury_Holiday(models.Model):
    category = models.CharField(('Категория'), max_length=20)
    created_at = models.DateTimeField(('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = 'Категория-Росскошный оддых'
        verbose_name_plural = 'Категории-Росскошных оддыхов'
        ordering = ['-id']


# Роскошный отдых
class Luxury_Holiday(models.Model):
    category = models.ForeignKey(Category_Luxury_Holiday, on_delete=models.CASCADE, related_name='luxury_holidays', verbose_name='Категория')
    image = models.ImageField(('Изображение'), upload_to='luxury_holiday_images/')
    title = models.CharField(('Заголовок'), max_length=255)
    created_at = models.DateTimeField(('Дата создания'), auto_now_add=True)

    def __str__(self):
        return f"Luxury Holiday Image {self.id}"
    
    class Meta:
        verbose_name = 'Роскошный отдых'
        verbose_name_plural = 'Роскошные отдыхи'
        ordering = ['-id']  


# Интервью
class Interview(models.Model):
    title = models.CharField(('Заголовок'), max_length=255)
    autor = models.CharField(('Автор'), max_length=255)
    studio = models.CharField(('Студия'), max_length=255)
    created_at = models.DateTimeField(('Дата создания'), auto_now_add=True)
    image = models.ImageField(('Изображение'), upload_to='interview_images/')

    def __str__(self):
        return f"Interview {self.title} by {self.autor}"
    
    class Meta:
        verbose_name = 'Интервью'
        verbose_name_plural = 'Интервью'
        ordering = ['-created_at'] 


# Продукты
class Product(models.Model):
    title = models.CharField(('Заголовок'), max_length=255)
    text = models.TextField(('Текст'))
    image = models.ImageField(('Изображение'), upload_to='Product_images/')
    created_at = models.DateTimeField(('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-id']  


# Предложения от компании
class CompanyOffer(models.Model):
    title = models.CharField(('Заголовок'), max_length=255)
    image = models.ImageField(('Изображение'), upload_to='CompanyOffer_images/')
    url = models.URLField(('URL'), blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Предложение от компании'
        verbose_name_plural = 'Предложения от компании'
        ordering = ['-id']  


# Статьи
class Article(models.Model):
    title = models.CharField(('Заголовок'), max_length=255)
    text = models.TextField(('Текст'))
    image = models.ImageField(('Изображение'), upload_to='Article_images/')
    created_at = models.DateTimeField(('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-id']  


# Отзывы
class Review(models.Model):
    name = models.CharField(('Имя'), max_length=30)
    review = models.TextField(('Отзыв'))
    object_id = models.IntegerField()
    created_at = models.DateTimeField(('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-id']  


# Блок "О нас"
class About(models.Model):
    title = models.CharField(('Заголовок'), max_length=255)
    image = models.ImageField(('Изображение'), upload_to='About_images/')
    created_at = models.DateTimeField(('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        ordering = ['-id']  


# О компании
class About_Company(models.Model):
    text = models.TextField(('О Компании'))
    image = models.ImageField(('Изображение'), upload_to='AboutCompany_images/')
    created_at = models.DateTimeField(('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.text[:50] + '...'
    
    class Meta:
        verbose_name = 'О Компании'
        verbose_name_plural = 'О Компании'
        ordering = ['-id']  


# Преимущества
class Advantage(models.Model):
    title = models.CharField(('Заголовок'), max_length=255)
    icon = models.ImageField(('Изображение'), upload_to='Advantage_images/', blank=True, null=True)
    order = models.PositiveIntegerField(('Сортировка'), default=0)
    created_at = models.DateTimeField(('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'
        ordering = ['order', '-created_at']



# Контактная информация
class ContactInfo(models.Model):
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
    image = models.ImageField(('Изображение'), upload_to='ContactInfo_images/')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return "Контактная информация"

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"
        ordering = ['-id']
