from django.shortcuts import render, redirect
from .models import Set, Word
from .set_form import SetForm
from .word_form import WordForm
# Create your views here.

def home(request):
    set_list = Set.objects.all()
    return render(request, 'home.html',{'set_list':set_list,})

def cards(request, pk):
    set = Set.objects.get(pk=pk)
    word_list =set.word_set.all() #主表.子表名稱小寫_set: 得到關聯單字
    return render(request, 'cards.html',{'set':set, 'word_list':word_list})

def set_new(request):
    if request.method == "POST":
        set_form = SetForm(request.POST)
        word_form = WordForm(request.POST)
        if set_form.is_valid() and word_form.is_valid():
            set = set_form.save(commit=False)
            word = word_form.save(commit=False)
            set.author = request.user
            set.save()
            word.word_set = set
            word.save()
            return redirect('/home/')
    else:
        set_form = SetForm()
        word_form = WordForm()
    return render(request, 'card_edit.html', {'set_form':set_form, 'word_form':word_form})