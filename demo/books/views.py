from django.shortcuts import render, redirect
from .models import books as book_model
from index.models import category as category_model  

# Create your views here.
def get_books(request, id):
    book_list = book_model.objects.filter(category_id = id)
    category = category_model.objects.get(category_id = id)
    return render(request, 'book.html', {'book_list' : book_list, 'category' : category})


def get_create_book(request):
    category_list = category_model.objects.filter()
    return render(request, 'add-book.html', {'category_list' : category_list})


def storeBook(request):
    if request.method == 'POST':
        category_id = request.POST['category']
        category = category_model.objects.get(category_id = category_id)

        name = request.POST['name']

        book = book_model.objects.create(category_id = category, name = name)
        book.save()

        return redirect('/category/' + str(category_id))
    else:
        return render(request, 'error.html')

def deleteBook(request, id):
    book = book_model.objects.filter(book_id = id)
    book.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def editBook(request, id):
    category_list = category_model.objects.filter()
    book = book_model.objects.get(book_id = id)

    return render(request, 'edit-book.html', {'category_list' : category_list, 'book' : book})

def updateBook(request, id):
    if request.method == 'POST':
        book = book_model.objects.get(book_id = id)

        category_id = request.POST['category']
        category = category_model.objects.get(category_id = category_id)

        name = request.POST['name']

        book.category_id_id = category_id
        book.name = name

        book.save()

        return redirect('/category/' + str(category_id))
    else:
        return render(request, 'error.html')