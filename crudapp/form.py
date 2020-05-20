from django import forms
from .models import Emp

class Empform(forms.ModelForm):
    eid = forms.IntegerField()
    ename = forms.CharField(max_length=15)
    eemail = forms.EmailField()
    ephnone_no = forms.CharField(max_length=15)
    class Meta:
        model = Emp
        fields = "__all__"

