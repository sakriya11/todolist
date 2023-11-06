from rest_framework import serializers
from todoapp.models import User
from todoapp.models import Todolist


# serializer for user model
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    conform_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def validate(self, data):
        if data["password"] != data["conform_password"]:
            raise serializers.ValidationError("Password did not match")
        return data


# serializer for  todolist model
class UserToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = "__all__"
