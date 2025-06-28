from django.urls import path
from config import settings
from django.conf.urls.static import static
from .views import (
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

urlpatterns = [
    path('popular/', PopularAPIView.as_view(), name='popular-list'),
    path('real-estate/', RealEstateAPIView.as_view(), name='real-estate-list'),
    path('luxury-holiday/', LuxuryHolidayAPIView.as_view(), name='luxury-holiday-list'),
    path('interviews/', InterviewAPIView.as_view(), name='interview-list'),
    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('company-offers/', CompanyOfferAPIView.as_view(), name='company-offer-list'),
    path('articles/', ArticleAPIView.as_view(), name='article-list'),
    path('reviews/', ReviewAPIView.as_view(), name='review-list-create'),  # GET и POST
    path('about/', AboutAPIView.as_view(), name='about-list'),
    path('about-company/', AboutCompanyAPIView.as_view(), name='about-company-list'),
    path('advantages/', AdvantageAPIView.as_view(), name='advantage-list'),
    path('contact-info/', ContactInfoAPIView.as_view(), name='contact-info-list'),
]

# Для загрузки медиафайлов в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
