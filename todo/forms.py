from django import forms

from .models import TodoItem


class TodoItemModelUpdateForm(forms.ModelForm):
    """
    ModelForm to update a single TodoItem 
    """
    class Meta:
        model = TodoItem
        fields = ('description', 'status',)

class TodoItemModelCreateForm(forms.ModelForm):
    """
    ModelForm to create a single TodoItem
    """
    success_url = '/todo/'
    class Meta:
        model = TodoItem
        fields = ('description', 'user',)
        