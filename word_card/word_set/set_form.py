from django import forms
from word_set.models import Set

#單字集的表單
class SetForm(forms.ModelForm):
    set_name = forms.CharField(label='表單標題', max_length=128)

    class Meta:
       model = Set
       fields = ['set_name']