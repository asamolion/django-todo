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

    def clean(self):
        cleaned_data = super(TodoItemModelUpdateForm, self).clean()
        status = cleaned_data.get('status')

        date_created = self.instance.date_created.replace(tzinfo=None)
        now = datetime.utcnow()
        date_created.time()
        delta = now - date_created
        days = delta.days  # days should be greater than 3g
        if (status == 'complete'):
            if days < 3:
                raise ValidationError(
                    _('Completion not yet allowed: days = %(value)s'),
                    code='too_quick',
                    params={'value': days},
                )
        return cleaned_data


class TodoItemModelCreateForm(forms.ModelForm):
    """
    ModelForm to create a single TodoItem
    """
    success_url = '/todo/'

    class Meta:
        model = TodoItem
        fields = ('description', 'user',)
