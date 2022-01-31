from dataclasses import field, fields
from pyexpat import model
from statistics import mode
from django.forms import ModelForm
from .models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'status', 'priority']

