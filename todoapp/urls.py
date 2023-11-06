from django.urls import path

from todoapp.views import (
    UserRegistrationView,
    updateUserList,
    updateUserListStatus,
    deleteUserList,
    getIndividualUserList,
)
from todoapp.views import createUserList

urlpatterns = [
    path("registration/", UserRegistrationView, name="registration"),
    path("create/todolist/", createUserList, name="todolist"),
    path("update/todolist/<int:pk>/", updateUserList, name="updatetodolist"),
    path(
        "update/todolist/status/<int:pk>/",
        updateUserListStatus,
        name="updateUserListStatus",
    ),
    path("delete/todolist/<int:pk>/", deleteUserList, name="deleteUserList"),
    path(
        "get/data/<int:user_id>",
        getIndividualUserList,
        name="getIndividualUserList",
    ),
]
