from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.


class TodoItem(models.Model):
    """
    Model that defines each entry in the todo list
    """
    description = models.CharField(max_length=256)
    date_created = models.DateTimeField(
        'Date created', auto_now_add=True)  # auto updation
    date_completed = models.DateTimeField(
        'Date completed', blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    status_choices = (
        ('inprogress', 'In Progress'),
        ('complete', 'Complete'),
        ('pending', 'Pending'),
    )
    status = models.CharField(max_length=32,
                              choices=status_choices,
                              default='pending')

    def __str__(self):
        return self.description
    
    # def clean(self):
    #     if self.status == 'pending':
    #         print('hello')
    #     else:
    #         print('nothello')
    #         raise ValidationError
    class Meta:
        permissions = (('is_manager', 'manager perms'),)
