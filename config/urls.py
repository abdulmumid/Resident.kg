from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Resident.kg API",
        default_version='v1',
        description=(
            "Resident.kg — строительная компания, основанная на традициях кыргызского гостеприимства и национальной культуры.\n\n"
            "Наша миссия — создавать качественные, надёжные и современные объекты недвижимости, которые способствуют процветанию клиентов и сотрудников.\n"
            "Главная цель — превзойти ожидания наших гостей и партнёров, обеспечивая высокий уровень сервиса на каждом этапе сотрудничества.\n\n"
            "### 📦 Основные модули:\n"
            "- 📸 **Popular** — популярные изображения\n"
            "- 🏠 **Real_Estate** — недвижимость\n"
            "- 🏖 **Luxury_Holiday** — роскошный отдых\n"
            "- 🎤 **Interview** — интервью\n"
            "- 🍱 **Product** — продукты\n"
            "- 💼 **CompanyOffer** — предложения от компании\n"
            "- 📰 **Article** — статьи\n"
            "- 💬 **Review** — отзывы\n"
            "- 🏢 **About** — 'О нас'\n"
            "- 🏭 **About_Company** — информация о компании\n"
            "- ⭐ **Advantage** — преимущества\n"
            "- 📞 **ContactInfo** — контактная информация\n\n"
            "### 🧰 Технологии:\n"
            "- Django, Django REST Framework\n"
            "- PostgreSQL\n"
            "- Swagger (drf-yasg)\n\n"
            "Все эндпоинты доступны через интерфейс Swagger, где их можно тестировать."
        ),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # логин
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # обновить access
    path('ckeditor/', include('ckeditor_uploader.urls')), 
    path('api/', include('API.urls')),  
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)