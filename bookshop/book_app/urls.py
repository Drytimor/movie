from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_book_all, name='book_all')
]