from django import forms
from.models import *

class TalabaForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=50, label="Ism")
    nums_of_books = forms.IntegerField(min_value=0, max_value=9, label="Kitob soni")
    course = forms.IntegerField(min_value=1, max_value=7)
    senior = forms.BooleanField(required=False)

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = "__all__"

class DateInput(forms.DateInput):
    input_type = 'date'

class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        widgets = {'tugilgan_yili':DateInput()}
        fields = "__all__"

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        widgets = {"olingan_sana":DateInput(), "qaytargan_sana":DateInput()}
        fields = "__all__"

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"