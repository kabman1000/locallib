from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #specifies path to its index view 
    path('books/', views.BookListView.as_view(), name='books'), #specifies path to its Books views
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]