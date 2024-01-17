from django.db import models


# user model
class User(models.Model):
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    conform_password = models.CharField(max_length=50)
    image = models.CharField(max_length=100, null=True)


# list model
class Todolist(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True
    )  # cascade is to delete the list if user is deleted
    title = models.CharField(max_length=70)
    # lists = models.TextField()
    status = models.BooleanField(default=False)
    todoTypes = models.CharField(max_length=15, null=True)
