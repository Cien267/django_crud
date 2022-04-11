from django.shortcuts import render
from .models import category as category_model

# Create your views here.
def get_index(request):
    category_list = category_model.objects.filter().order_by('category_id')
    return render(request, 'index.html', {'category_list' : category_list})