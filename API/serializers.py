from rest_framework import serializers
from .models import (
    Popular, Category_Real_Estate, Real_Estate, Category_Luxury_Holiday, Luxury_Holiday, Interview,
    Product, CompanyOffer, Article, Review, About,
    About_Company, Advantage, ContactInfo
)

class PopularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Popular
        fields = '__all__'


class CategoryRealEstate(serializers.ModelSerializer):
    class Meta:
        model = Category_Real_Estate
        fields = '__all__'


class RealEstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Real_Estate
        fields = '__all__'


class CategoryLuxuryHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_Luxury_Holiday
        fields = '__all__'


class LuxuryHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Luxury_Holiday
        fields = '__all__'


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CompanyOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyOffer
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Company
        fields = '__all__'


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'
