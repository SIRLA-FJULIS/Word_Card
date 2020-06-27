from django.shortcuts import render
from .models import Set, Word
from .set_form import SetForm
# Create your views here.

def home(request):
    set_list = Set.objects.all()
    return render(request, 'home.html',{'set_list':set_list,})
