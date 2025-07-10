from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    UserRegistrationViewSet,
    PopularAPIView,
    RealEstateAPIView,
    LuxuryHolidayAPIView,
    InterviewAPIView,
    ProductAPIView,
    CompanyOfferAPIView,
    ArticleAPIView,
    ReviewAPIView,
    AboutAPIView,
    AboutCompanyAPIView,
    AdvantageAPIView,
    ContactInfoAPIView,
)

router = DefaultRouter()
router.register(r'users', UserRegistrationViewSet, basename='user')

urlpatterns = [
    # Токен для аутентификации DRF (если нужен)
    path('api-token-auth/', obtain_auth_token),

    # Все CRUD операции с пользователями
    path('', include(router.urls)),

    # Остальные API
    path('popular/', PopularAPIView.as_view(), name='popular-list'),
    path('real-estate/', RealEstateAPIView.as_view(), name='real-estate-list'),
    path('luxury-holiday/', LuxuryHolidayAPIView.as_view(), name='luxury-holiday-list'),
    path('interviews/', InterviewAPIView.as_view(), name='interview-list'),
    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('company-offers/', CompanyOfferAPIView.as_view(), name='company-offer-list'),
    path('articles/', ArticleAPIView.as_view(), name='article-list'),
    path('reviews/', ReviewAPIView.as_view(), name='review-list-create'),  # POST и (если надо) GET
    path('about/', AboutAPIView.as_view(), name='about-list'),
    path('about-company/', AboutCompanyAPIView.as_view(), name='about-company-list'),
    path('advantages/', AdvantageAPIView.as_view(), name='advantage-list'),
    path('contact-info/', ContactInfoAPIView.as_view(), name='contact-info-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
