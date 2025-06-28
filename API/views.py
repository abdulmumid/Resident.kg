from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


# Популярное
class PopularAPIView(APIView):
    def get(self, request):
        queryset = Popular.objects.all().order_by('-id')
        serializer = PopularSerializer(queryset, many=True)
        return Response(serializer.data)


#Категория-Недвижимость
class CategoryRealEstateAPIView(APIView):
    def get(self, request):
        queryset = Category_Real_Estate.objects.all().order_by('-id')
        serializer = CategoryLuxuryHolidaySerializer(queryset, many=True)
        return Response(serializer.data)


# Недвижимость
class RealEstateAPIView(APIView):
    def get(self, request):
        queryset = Real_Estate.objects.all().order_by('-id')
        serializer = RealEstateSerializer(queryset, many=True)
        return Response(serializer.data)


#Категория-Росскошный оддых
class CategoryLuxuryHolidayAPIView(APIView):
    def get(self, request):
        queryset = Category_Luxury_Holiday.objects.all().order_by('-id')
        serializer = CategoryLuxuryHolidaySerializer(queryset, many=True)
        return Response(serializer.data)


# Роскошный отдых
class LuxuryHolidayAPIView(APIView):
    def get(self, request):
        queryset = Luxury_Holiday.objects.all().order_by('-id')
        serializer = LuxuryHolidaySerializer(queryset, many=True)
        return Response(serializer.data)


# Интервью
class InterviewAPIView(APIView):
    def get(self, request):
        queryset = Interview.objects.all().order_by('-id')
        serializer = InterviewSerializer(queryset, many=True)
        return Response(serializer.data)


# Продукты
class ProductAPIView(APIView):
    def get(self, request):
        queryset = Product.objects.all().order_by('-id')
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


# Предложения от компании
class CompanyOfferAPIView(APIView):
    def get(self, request):
        queryset = CompanyOffer.objects.all().order_by('-id')
        serializer = CompanyOfferSerializer(queryset, many=True)
        return Response(serializer.data)


# Статьи
class ArticleAPIView(APIView):
    def get(self, request):
        queryset = Article.objects.all().order_by('-id')
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)


# Отзывы
class ReviewAPIView(APIView):
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Блок "О нас"
class AboutAPIView(APIView):
    def get(self, request):
        queryset = About.objects.all().order_by('-id')
        serializer = AboutSerializer(queryset, many=True)
        return Response(serializer.data)


# О компании
class AboutCompanyAPIView(APIView):
    def get(self, request):
        queryset = About_Company.objects.all().order_by('-id')
        serializer = AboutCompanySerializer(queryset, many=True)
        return Response(serializer.data)


# Преимущества
class AdvantageAPIView(APIView):
    def get(self, request):
        queryset = Advantage.objects.all().order_by('-id')
        serializer = AdvantageSerializer(queryset, many=True)
        return Response(serializer.data)


# Контактная информация
class ContactInfoAPIView(APIView):
    def get(self, request):
        queryset = ContactInfo.objects.all().order_by('-id')
        serializer = ContactInfoSerializer(queryset, many=True)
        return Response(serializer.data)
