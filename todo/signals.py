from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


from todo.models import TodoItem


@receiver(post_save, sender=TodoItem)
def log_todoitem(sender, **kwargs):
    '''
    Logs the id, user and time of each TodoItem after each save
    '''
    with open('todo_update_log.txt', 'a') as log:
        log.write('Task: %s | User: %s | Time: %s\n' % (
            kwargs['instance'].id, kwargs['instance'].user, timezone.now()
        ))
    
