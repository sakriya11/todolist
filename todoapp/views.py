from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from todoapp.serializations import (
    UserToDoListSerializer,
    UserLoginSerializer,
    RegistrationSerializer,
    UsertodolistStatus,
)
from todoapp.models import Todolist
from django.contrib.auth import authenticate
from rest_framework import views, status
from rest_framework.authtoken.models import Token


# user registration
@api_view(["POST"])
def UserRegistrationView(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        print("dataaaaaaaaaaaaa", request.data)
        if serializer.is_valid():
            user = serializer.save()
            userData = RegistrationSerializer(user).data
            return Response(
                {"message": "User registration successful", "data": userData},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# user login
# class UserLogin(views.APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         email = serializer.validated_data["email"]
#         password = serializer.validated_data["password"]

#         user = authenticate(request, email=email, password=password)

#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key}, status=status.HTTP_200_OK)
#         else:
#             return Response(
#                 {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
#             )


# to fetch the individual users lists
@api_view(["GET"])
def getIndividualUserList(request, user_id):
    try:
        todolist = Todolist.objects.filter(user_id=user_id)
    except Todolist.DoesNotExist:
        return Response(
            {"message": "user todo list does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        serializer = UserToDoListSerializer(todolist, many=True)
        return Response(
            {"message": "Data retrived succesfully", "data": serializer.data},
            status=status.HTTP_200_OK,
        )


# to create user list
@api_view(["POST"])
def createUserList(request):
    if request.method == "POST":
        serializer = UserToDoListSerializer(data=request.data)
        if serializer.is_valid():
            todolist = serializer.save()
            todolistData = UserToDoListSerializer(todolist).data
            return Response(
                {"message": "List created succesfully", "data": todolistData},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# to update user list
@api_view(["PATCH"])
def updateUserList(request, pk):
    try:
        todolist = Todolist.objects.get(pk=pk)
    except Todolist.DoesNotExist:
        return Response(
            {"message": "Following list does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "PATCH":
        serializer = UserToDoListSerializer(todolist, data=request.data, partial=True)
        if serializer.is_valid():
            updatedTodolist = serializer.save()
            updatedTodolistData = UserToDoListSerializer(updatedTodolist).data
            return Response(
                {"message": "Data updated succesfully", "data": updatedTodolistData},
                status=status.HTTP_201_CREATED,
            )


# to update the user list status
@api_view(["PATCH"])
def updateUserListStatus(request, pk):
    try:
        todolist = Todolist.objects.get(pk=pk)
    except Todolist.DoesNotExist:
        return Response(
            {"message": "Following list does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "PATCH":
        serializer = UserToDoListSerializer(todolist, data=request.data, partial=True)
        if serializer.is_valid():
            updatedTodolist = serializer.save()
            updatedTodolistData = UserToDoListSerializer(updatedTodolist).data
            return Response(
                {"message": "Data updated succesfully", "data": updatedTodolistData},
                status=status.HTTP_201_CREATED,
            )


# to delete the user list
@api_view(["DELETE"])
def deleteUserList(request, pk):
    try:
        todolist = Todolist.objects.get(pk=pk)
    except Todolist.DoesNotExist:
        return Response(
            {"message": "Following list does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "DELETE":
        todolist.delete()
        return Response(
            {"message": "List deleted succesfully"},
            status=status.HTTP_201_CREATED,
        )


# to fetch the all users lists
@api_view(["GET"])
def getAllUserList(request):
    try:
        todolist = Todolist.objects.all()
    except Todolist.DoesNotExist:
        return Response(
            {"message": "user todo list does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        serializer = UserToDoListSerializer(todolist, many=True)

        return Response(
            {"message": "Data retrived succesfully", "data": serializer.data},
            status=status.HTTP_200_OK,
        )


# to fetch the individual users lists
@api_view(["GET"])
def getIndividualUserList(request, pk):
    try:
        todolist = Todolist.objects.get(pk=pk)
    except Todolist.DoesNotExist:
        return Response(
            {"message": "user todo list does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "GET":
        serializer = UserToDoListSerializer(todolist)

        return Response(
            {"message": "Data retrived succesfully", "data": serializer.data},
            status=status.HTTP_200_OK,
        )


# to filter the list in basis of todo status
@api_view(["GET"])
def getTodoListStatus(request, statusQuery):
    try:
        if statusQuery == "all":
            todolistStatus = Todolist.objects.all()
            serializer = UsertodolistStatus(todolistStatus, many=True)

            return Response(
                {"message": "Data retrived succesfully", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

        todolistStatus = Todolist.objects.filter(status=statusQuery)
        if not (todolistStatus):
            return Response(
                {"message": "User todo list does not exist for the given status"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if request.method == "GET":
            serializer = UsertodolistStatus(todolistStatus, many=True)

            return Response(
                {"message": "Data retrived succesfully", "data": serializer.data},
                status=status.HTTP_200_OK,
            )

    except Todolist.DoesNotExist:
        return Response(
            {"message": "user todo list does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )
