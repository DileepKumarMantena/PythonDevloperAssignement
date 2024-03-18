from django.shortcuts import render

# Create your views here.
from .Books_Crud.add_books_post import BokksPostApi
from .Books_Crud.delete_book_api import DeleteBook
from .Books_Crud.get_books import GetBooks
from .Books_Crud.update_books_api import BooksUpdate

from .Review_Crud.review_post_api import ReviewPostApi
from .Review_Crud.review_get_api import ReviewGetApi
from .Review_Crud.update_review_api import ReviewUpdateApi
from .Review_Crud.review_delete_api import DeleteReview





BokksPostApi()
DeleteBook()
GetBooks()
BooksUpdate()

ReviewPostApi()
ReviewGetApi()
ReviewUpdateApi()
DeleteReview()


