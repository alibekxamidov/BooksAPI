from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'content', 'title', 'subtitle', 'author', 'isbn', 'price',)


    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitob nomi harflardan iborat bo'lishi kerak"
                }
            )

        if Book.objects.filter(title=title, author=author).exits():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Muallif va kitob nomi bir xil bo'lishi mumkin emas"
                }
            )