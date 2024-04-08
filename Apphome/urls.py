from django.urls import path
from .views import BookListApiView, BookListCreateApiView, BookUpdateApiView, BookDeleteApiView, BookDetailApiView, BookViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('books/', BookListApiView.as_view()),
    # path('books/create/', BookListCreateApiView.as_view()),
    # path('books/<int:pk>', BookDetailApiView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateApiView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteApiView.as_view())


]
urlpatterns = urlpatterns + router.urls