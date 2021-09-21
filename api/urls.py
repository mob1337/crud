from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

path('rest/books/',views.BookList.as_view()),
    path('rest/books/<int:pk>', views.BookDetail.as_view(), name="Detail"),

]