from django.shortcuts import render
from .models import Set, Word
from .set_form import SetForm
# Create your views here.

def home(request):
    set_list = Set.objects.all()
    return render(request, 'home.html',{'set_list':set_list,})

def cards(request, pk):
    set = Set.objects.get(pk=pk)
    word_list =set.word_set.all() #主表.子表名稱小寫_set: 得到關聯單字
    return render(request, 'cards.html',{'set':set, 'word_list':word_list})

