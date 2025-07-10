from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta
from .models import *
from .serializers import *


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data.get('password')
        serializer.save(password=make_password(password))

    def perform_update(self, serializer):
        password = serializer.validated_data.get('password')
        if password:
            serializer.save(password=make_password(password))
        else:
            serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(password=make_password(serializer.validated_data['password']))

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        access.set_exp(lifetime=timedelta(minutes=60))

        data = {
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(access),
        }
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


# Популярное
class PopularAPIView(APIView):
    def get(self, request):
        queryset = Popular.objects.all().order_by('-id')
        serializer = PopularSerializer(queryset, many=True)
        return Response(serializer.data)


# Категория - Недвижимость
class CategoryRealEstateAPIView(APIView):
    def get(self, request):
        queryset = CategoryRealEstate.objects.all().order_by('-id')
        serializer = CategoryRealEstateSerializer(queryset, many=True)
        return Response(serializer.data)


# Недвижимость
class RealEstateAPIView(APIView):
    def get(self, request):
        queryset = RealEstate.objects.all().order_by('-id')
        serializer = RealEstateSerializer(queryset, many=True)
        return Response(serializer.data)


# Категория - Роскошный отдых
class CategoryLuxuryHolidayAPIView(APIView):
    def get(self, request):
        queryset = CategoryLuxuryHoliday.objects.all().order_by('-id')
        serializer = CategoryLuxuryHolidaySerializer(queryset, many=True)
        return Response(serializer.data)


# Роскошный отдых
class LuxuryHolidayAPIView(APIView):
    def get(self, request):
        queryset = LuxuryHoliday.objects.all().order_by('-id')
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


# Отзывы (POST только)
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
        queryset = AboutCompany.objects.all().order_by('-id')
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
