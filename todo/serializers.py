from rest_framework import serializers
from todo.models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('description', 'user', 'date_created',
                  'status', 'date_completed', )
