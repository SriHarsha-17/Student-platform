from rest_framework.serializers import *
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from courses.models.course import Course

class CourseSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=100,validators =[UniqueValidator(queryset= Course.objects.all(),message="Course must be unique")])
    code = CharField(validators =[UniqueValidator(queryset= Course.objects.all(),message="Code must be unique")])
    description = CharField(max_length=600)

    # class Meta:
    #     validators = [
    #         UniqueTogetherValidator(
    #             queryset = Course.objects.all(),
    #             fields = ['name','code'],
    #             message="Every course must have a unique name and code"
    #         )
    #     ]
        
    def create(self, validated_data):
        """Create and re turn a new `Course` instance, given the validated data."""
        return Course.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.code = validated_data.get("code", instance.code)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance