from rest_framework import serializers
from api.models import Book
import datetime

"""
Serializer for the book model.
Adds:
        - A validation for the publication year not being greater than the current year.
"""

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required = True, allow_blank = True, max_length = 200)
    publication_year = serializers.IntegerField(required = True, max_length = 4, default=2025)
    author = serializers.CharField(required = True, max_length = 200)
    
    
    def validate_pub_year(self, value):
        if value > datetime:
            raise serializers.ValidationError("Publication year cannot be greater than current Year.")
        return value

"""
    Serializer for the Author Model.    
"""

class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required = True, max_length = 200)
    