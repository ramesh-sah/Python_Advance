from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Student List API


@csrf_exempt
@api_view(['GET'])
def student_list_view(request):

    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data, safe=False)


# Student Create API

@csrf_exempt
@api_view(['POST'])
def student_create_view(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Student Retrieve API


@csrf_exempt
@api_view(['GET'])
def student_retrieve_view(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(student)
    return JsonResponse(serializer.data, safe=False)

# Student Update API


@csrf_exempt
@api_view(['PUT'])
def student_update_view(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    data = JSONParser().parse(request)
    serializer = StudentSerializer(instance=student, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Student Partial Update API


@csrf_exempt
@api_view(['PATCH'])
def student_partial_update_view(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    data = JSONParser().parse(request)
    serializer = StudentSerializer(instance=student, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Student Delete API


@csrf_exempt
@api_view(['DELETE'])
def student_delete_view(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    student.delete()
    return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
