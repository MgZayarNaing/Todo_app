from django.shortcuts import render
from my_app.serializer import  TaskSerializer
from my_app.models import  TaskModel

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 1000