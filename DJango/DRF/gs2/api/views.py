from django.shortcuts import render
import io
from .serializers import StudentSerializers
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "data created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
