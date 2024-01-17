from django.urls import path

from todoapp.views import (
    UserRegistrationView,
    updateUserList,
    updateUserListStatus,
    deleteUserList,
    getIndividualUserList,
    UserLogin,
    getAllUserList,
    getTodoListStatus,
)
from todoapp.views import createUserList


urlpatterns = [
    path("registration/", UserRegistrationView, name="registration"),
    path("login/", UserLogin.as_view(), name="api-login"),
    path("create/todolist/", createUserList, name="todolist"),
    path("update/todolist/<int:pk>/", updateUserList, name="updatetodolist"),
    path(
        "update/todolist/status/<int:pk>/",
        updateUserListStatus,
        name="updateUserListStatus",
    ),
    path("delete/todolist/<int:pk>/", deleteUserList, name="deleteUserList"),
    path(
        "get/data/<int:pk>/",
        getIndividualUserList,
        name="getIndividualUserList",
    ),
    path(
        "get/data/",
        getAllUserList,
        name="getAllUserList",
    ),
    path(
        "get/status/data/<str:statusQuery>/",
        getTodoListStatus,
        name="getTodoListStatus",
    ),
]
