from django.contrib import admin
from django.urls import path
from api.views import BookListCreateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', BookListCreateAPIView.as_view(),
name="book_list_view")
]
