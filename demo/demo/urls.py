"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from index import views as index
from books import views as books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.get_index),
    path('category/<int:id>/', books.get_books),
    path('addBook/', books.get_create_book),
    path('storeBook', books.storeBook),
    path('book/delete/<int:id>/', books.deleteBook),
    path('book/edit/<int:id>/', books.editBook),
    path('book/update/<int:id>', books.updateBook),
]
admin.site.site_header = "TEST"