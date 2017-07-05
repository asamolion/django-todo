from rest_framework import serializers
from todo.models import TodoItem
from django.contrib.auth.models import User


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('description', 'user', 'date_created',
                  'status', 'date_completed', )


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=TodoItem.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
