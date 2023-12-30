from django.shortcuts import render

from .mypagination import MyPageNumberPagination, MyLimitOffsetPagination, MyCusrsorPagination
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class StudentView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name']
    # filter_backends = [OrderingFilter]
    pagination_class = MyCusrsorPagination

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)
