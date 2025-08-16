from rest_framework import serializers
from api.models import Book, Author
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

"""
Serializer for the book model.
Adds:
        - A validation for the publication year not being greater than the current year.
"""

class BookSerializer(serializers.ModelSerializer):
            
        title = serializers.CharField(required = True, max_length = 200)
        publication_year = serializers.IntegerField(required = True, 
                                                    
                                                    validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.date.today().year)
        ]
        )
        
        author = serializers.CharField(required = False, max_length = 200)
        
        
        def validate_publication_year(self, value):
            if value > datetime.date.today().year:
                raise serializers.ValidationError("Publication year cannot be greater than current Year.")
            return value
        
        class Meta:
        
            model = Book
            fields = "__all__"
"""
    Serializer for the Author Model.    
"""

class AuthorSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(read_only=True)
    class Meta:
        model = Author
        fields = "__all__"
        
    