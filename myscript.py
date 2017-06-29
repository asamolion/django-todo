'''
Script to bulk create 20 random users and randomly assign 500 tasks to them
'''
import random
import string

from todo.models import TodoItem
from django.contrib.auth.models import User


# UTILITY FUNCTIONS
def randomword(length):
    '''
    returns a random word of size 'length'
    '''
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


for i in range(20):
    username = randomword(5)
    # password = 'arbisoft123'
    user = User.objects.create_user(
        username, password='arbisoft123'
    )
    if created:
        task_list = []
        for j in range(25):
            task_list.append(TodoItem(description=randomword(25), user=user))
        TodoItem.objects.bulk_create(task_list)
