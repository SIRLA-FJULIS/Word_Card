from django import forms
from word_set.models import Set

#單字集的表單
class SetForm(forms.ModelForm):
    name = forms.CharField(label='標題', max_length=128)

   class Meta:
       model = word_set
       fields = ['name']