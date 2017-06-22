from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class TodoItem(models.Model):
    description = models.CharField(max_length=256)
    date_created = models.DateTimeField(
        'Date created', auto_now_add=True)  # auto updation
    date_completed = models.DateTimeField(
        'Date completed', blank=True, null=True)
    user = models.ForeignKey(User, default=1)
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

    # class Meta:
    #     permissions = (('can_todo', 'set todo'),)
