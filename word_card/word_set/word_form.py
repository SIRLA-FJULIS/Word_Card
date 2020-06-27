from django import forms
from word_set.models import Word

#單字的表單
class WordForm(forms.ModelForm):
    word = forms.CharField(label='英文', max_length=128)
    chinese = forms.CharField(label='中文', max_length=128)


    class Meta:
       model = Word
       fields = ['word', 'chinese']
