from rest_framework.serializers import *
from courses.models.course import Course

class CourseSerializer(Serializer):
    name = CharField(max_length=100)
    code = CharField()
    description = CharField(max_length=600)

    def create(self, validated_data):
        """Create and re turn a new `Course` instance, given the validated data."""
        return Course.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.code = validated_data.get("code", instance.code)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance