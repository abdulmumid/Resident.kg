from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class PopularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Popular
        fields = '__all__'


class CategoryRealEstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryRealEstate
        fields = '__all__'


class RealEstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields = '__all__'


class CategoryLuxuryHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryLuxuryHoliday
        fields = '__all__'


class LuxuryHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = LuxuryHoliday
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
        model = AboutCompany
        fields = '__all__'


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'
