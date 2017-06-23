from django import forms
from datetime import datetime
from .models import TodoItem


class TodoItemModelUpdateForm(forms.ModelForm):
    """
    ModelForm to update a single TodoItem 
    """
    class Meta:
        model = TodoItem
        fields = ('description', 'status',)

    """
    DEAL WITH THIS LATER

    def clean(self):
        cleaned_data = super(TodoItemModelUpdateForm, self).clean()
        status = cleaned_data.get('status')

        date_created = self.instance.date_created
        now = datetime.utcnow()
        print(date_created)
        print(type(date_created))
        print(now)
        print(type(now))
    """

class TodoItemModelCreateForm(forms.ModelForm):
    """
    ModelForm to create a single TodoItem
    """
    success_url = '/todo/'

    class Meta:
        model = TodoItem
        fields = ('description', 'user',)
