from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import Bookserializer
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView


# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Bookserializer




class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serilazer_data = Bookserializer(books, many=True).data
        data = {
            'status': f"Returned {len(books)} books",
            'books': serilazer_data
        }
        return Response(data)

# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Bookserializer


class BookDetailApiView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serilazer_data = Bookserializer(book).data
            data = {
                'status': 'Succesfull',
                'book': serilazer_data
            }
            return Response(data)
        except Exception:
            return Response(
                {
                    'status': 'Does not exits',
                    'message': 'Book is not found'
                    },
                status=status.HTTP_404_NOT_FOUND
            )


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Bookserializer

class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response(
                {
                    'status': True,
                    'Message': 'successfully delete'
                },
                status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    'status': False,
                    'Meesage': 'Book is not found'
                },
                status=status.HTTP_400_BAD_REQUEST
            )





# class BookdeleteApiView(generics.RetrieveDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Bookserializer

class BookUpdateApiView(APIView):

    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk )
        data = request.data
        serilazer = Bookserializer(instance=book, data=data, partial=True)
        if serilazer.is_valid(raise_exception=True):
            book_saved = serilazer.save()
        return Response(
            {
                'status': True,
                'message': f"Book {book_saved} update successfully"
            }
        )


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Bookserializer


class BookListCreateApiView(APIView):

    def create(self, request):
        data = request.data
        serilazer = Bookserializer(data=data)
        if serilazer.is_valid():
            serilazer.save()
            data = {

                    'status': f"Book save database",
                    'books': data
            }
            return Response(data)




# class BookListCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Bookserializer

