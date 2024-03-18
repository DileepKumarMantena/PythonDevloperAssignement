from django.urls import path
from .views import *

urlpatterns = [
    path('BokksPostApi/', BokksPostApi.as_view()),
    path('GetBooks/',GetBooks.as_view()),
    path('BokksPostApi/', BokksPostApi.as_view()),
    path('BooksUpdate/<int:id>/', BooksUpdate.as_view()),
    path('DeleteBook/<int:id>/', DeleteBook.as_view()),
    path('ReviewPostApi/', ReviewPostApi.as_view()),
    path('ReviewGetApi/<int:id>/', ReviewGetApi.as_view()),
    path('DeleteReview/<int:id>/', DeleteReview.as_view()),
    path('ReviewUpdateApi/<int:id>/', ReviewUpdateApi.as_view()),
]

BokksPostApi()
DeleteBook()
GetBooks()
BooksUpdate()

ReviewPostApi()
ReviewGetApi()
ReviewUpdateApi()
DeleteReview()