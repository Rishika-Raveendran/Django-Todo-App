from django import forms
from django.forms import ModelForm
from .models import *
# from bootstrap_modal_forms.forms import BSModalModelForm


class TaskForm(forms.ModelForm):
    # Needs atleast two values. The model for which form is being created, and the field
    class Meta:
        model = Task
        fields = "__all__"

