from django.apps import apps
from rest_framework import serializers

from .models import *


class BookPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = "__all__"

    def create(self, validated_data):
        user = BooksModel.objects.create(Title=validated_data['Title'],
                                        Author=validated_data['Author'],
                                        Date_Field=validated_data['Date_Field'],
                                    )

        user.save()
        return user

class MembersGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = "__all__"



class ReviewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = "__all__"

    def create(self, validated_data):
        user = ReviewModel.objects.create(Review_Text=validated_data['Review_Text'],
                                        Rating=validated_data['Rating'],
                                        Date_Field=validated_data['Date_Field'],
                                        BookId=validated_data['BookId']
                                    )

        user.save()
        return user

class ReviewGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = "__all__"