from django import forms
from .models import Researcher, Degree, PosDegree
from django.forms.widgets import CheckboxSelectMultiple
from django.forms import ModelMultipleChoiceField
from easy_select2.widgets import Select2Multiple
from django_select2.forms import Select2TagWidget
from easy_select2 import select2_modelform

ResearcherForm2 = select2_modelform(Researcher, attrs={'width': '250px'})

class ResearcherForm(forms.ModelForm):
    form = ResearcherForm2
    class Meta():
        model = Researcher
        fields = ['first_name', 'last_name', 'category', 'degree', 'pos_degree']

        widgets = {'first_name' : forms.PasswordInput,
                   'degree' : Select2Multiple()}
    # degree = ModelMultipleChoiceField(widget=CheckboxSelectMultiple, required=True, queryset=Degree.objects.all())
    # pos_degree = ModelMultipleChoiceField(widget=Select2Multiple, required=True, queryset=PosDegree.objects.all())