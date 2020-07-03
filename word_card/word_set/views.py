from django.shortcuts import render, redirect, get_object_or_404
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
        if set_form.is_valid():
            set = set_form.save(commit=False)
            set.author = request.user
            set.save()
            word = request.POST.getlist('word')
            chinese = request.POST.getlist('chinese')
            for w, c in zip(word, chinese):
                words = Word(word_set = set, word = w, chinese = c)
                words.save()
            return redirect('cards', pk=set.pk)
    else:
        set_form = SetForm()
    return render(request, "card_new.html", {'set_form':set_form})

def set_edit(request, pk):
    set = get_object_or_404(Set, pk=pk)
    if request.method == "POST":
        set_form = SetForm(request.POST, instance=set)
        word_list = set.word_set.all()
        for i in word_list:
            print(i.word)
            print(i.chinese)
        if set_form.is_valid():
            set = set_form.save(commit=False)
            # set.author = request.user #加上這句就不行
            set.save()
            return redirect('cards', pk=set.pk)
    else:
        set_form = SetForm(instance=set)
    return render(request, 'card_edit.html', {'set_form':set_form})

def set_delete(request, pk):
    set = Set.objects.get(pk=pk)
    set.delete()
    return redirect('home')