from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework.mixins import *
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from api.customauth import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle


# Create your views here.


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    authentication_classes = [SessionAuthentication]
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "viewstu"


# class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializers

# class StudentViewSet(viewsets.ViewSet):
#     def list(self, request):
#         stu = Student.objects.all()
#         serializer = StudentSerializers(stu, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def retrieve(self, request, pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializers(stu)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def create(self, request):
#         serializer = StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': "data created"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, pk=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializers(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": "data update complete"}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializers(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": "data update complete"}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({"msg": "data deleted"}, status=status.HTTP_204_NO_CONTENT)


# class PCStudentAPI(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers


# class RUDStudentAPI(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

# class PCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def hello_world(request):
#     if request.method == "GET":
#         return Response({"msg": "this is get method "})
#     elif request.method == "POST":
#         return Response({"msg": "this is the post method"})
#     elif request.method == "PUT":
#         return Response({"msg": "this is put method "})
# @api_view(['GET', "POST", "PUT", "PATCH", "DELETE"])
# class StudentAPI(APIView):
#     def get(self, request, pk=None, format=None):
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk=id)
#             serializer = StudentSerializers(stu)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         stu = Student.objects.all()
#         serializer = StudentSerializers(stu, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, pk=None, format=None):
#         serializer = StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Msg": 'created success'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk=None, format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializers(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': "data updated fully"}, status=status.HTTP_205_RESET_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk=None, format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializers(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg": "partial updated success"}, status=status.HTTP_206_PARTIAL_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk=None, format=None):
#         id = pk
#         stu = Student.objects.get(pk=id)
#         stu.delete()
#         return Response({"msg": "deleted successfully"}, status=status.HTTP_508_LOOP_DETECTED)


# def student_api(request, pk=None):
#     if request.method == "GET":
#         id = pk
#         if id is not None:
#             stu = Student.objects.get(pk=id)
#             serializer = StudentSerializers(stu)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         stu = Student.objects.all()
#         serializer = StudentSerializers(stu, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    # elif request.method == "POST":
    #     serializer = StudentSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"Msg": 'created success'}, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == "PUT":
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     serializer = StudentSerializers(stu, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': "data updated fully"}, status=status.HTTP_205_RESET_CONTENT)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == "PATCH":
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     serializer = StudentSerializers(stu, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"msg": "partial updated success"}, status=status.HTTP_206_PARTIAL_CONTENT)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == "DELETE":
    #     id = pk
    #     stu = Student.objects.get(pk=id)
    #     stu.delete()
    #     return Response({"msg": "deleted successfully"}, status=status.HTTP_508_LOOP_DETECTED)

    # else:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
