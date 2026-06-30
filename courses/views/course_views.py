from django.http import HttpResponse, JsonResponse
from courses.models.course import Course
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from courses.serializers.course_serializer import CourseSerializer


def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        #response = {"courses" : list(courses.values())}
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

def course_detail(request,pk):
    course = get_object_or_404(Course,pk=pk)
    serializer = CourseSerializer(course)
    return JsonResponse(serializer.data)