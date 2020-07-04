from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Set, Word
from .set_form import SetForm
from .word_form import WordForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        id = request.user.id
        set_list = Set.objects.filter(author_id=id) 
    else:
        set_list = Set.objects.all()
    return render(request, 'home.html',{'set_list':set_list,})

def cards(request, pk):
    set = Set.objects.get(pk=pk)
    word_list =set.word_set.all() #主表.子表名稱小寫_set: 得到關聯單字
    return render(request, 'cards.html',{'set':set, 'word_list':word_list})

def word_status(request, pk):
    word = Word.objects.get(pk=pk)
    if word.completed == True:
        word.completed = False
        word.save()
        responseData = {'msg':'False'}
    else:
        word.completed = True
        word.save()
        responseData = {'msg':'True'}
    return JsonResponse(responseData)

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
    word_list = set.word_set.all()
    if request.method == "POST":
        set_form = SetForm(request.POST, instance=set)
        if set_form.is_valid():
            set = set_form.save(commit=False)
            set.save()
            word_list.delete()
            word = request.POST.getlist('word')
            chinese = request.POST.getlist('chinese')
            for w, c in zip(word, chinese):            
                words = Word(word_set = set, word = w, chinese = c)
                words.save()
            return redirect('cards', pk=set.pk)
    else:
        set_form = SetForm(instance=set)
    return render(request, 'card_edit.html', {'set_form':set_form, 'word_list':word_list})

def set_delete(request, pk):
    set = Set.objects.get(pk=pk)
    set.delete()
    return redirect('home')


def login(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect('/home/')
    else:
        return render(request, 'login.html', locals())

    def logout(request):
        auth.logout(request)
        return redirect('/home/')

def register(request):
 if request.method == 'POST':
  form = UserCreationForm(request.POST)
  print("Errors", form.errors)
  if form.is_valid():
   form.save()
   return redirect('home')
  else:
    return render(request, 'registration/register.html', {'form':form})
 else:
  form = UserCreationForm()
  context = {'form': form}
  return render(request, 'registration/register.html', context)