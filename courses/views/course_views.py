from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from courses.models.course import Course
from django.shortcuts import get_object_or_404
from courses.serializers.course_serializer import CourseSerializer

@api_view(['GET','POST'])
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        #response = {"courses" : list(courses.values())}
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def course_detail(request,pk):

    course = get_object_or_404(Course,pk=pk)
    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        course.delete()
        return Response({"status":"Course deleted sucessfully"},status=HTTP_204_NO_CONTENT)