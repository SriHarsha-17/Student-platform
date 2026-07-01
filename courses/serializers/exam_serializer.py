from rest_framework.serializers import *
from courses.models.exam import Exam
from courses.serializers.course_serializer import CourseSerializer

class ExamSerializer(Serializer):
    course = CourseSerializer(read_only=True)
    course_id = IntegerField()
    title = SlugField()
    total_marks = IntegerField()
    date = DateTimeField()
    duration_minutes = IntegerField()

    def create(self, validated_data):
        """Create and re turn a new `Course` instance, given the validated data."""
        return Exam.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.total_marks = validated_data.get("total_marks", instance.total_marks)
        instance.date = validated_data.get("date", instance.date)
        instance.duration_minutes = validated_data.get("duration_minutes", instance.duration_minutes)
        instance.save()
        return instance