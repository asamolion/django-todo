from django import forms

from .models import TodoItem


class TodoItemModelUpdateForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ('description', 'status',)

class TodoItemModelCreateForm(forms.ModelForm):
    success_url = '/todo/'
    class Meta:
        model = TodoItem
        fields = ('description', 'user',)
        