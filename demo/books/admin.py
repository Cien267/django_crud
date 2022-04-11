from django.contrib import admin
from .models import books

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'category_id', 'name')
    search_fields = ['name']
    list_filter = ('book_id', 'category_id', 'name') 

admin.site.register(books, BookAdmin)
