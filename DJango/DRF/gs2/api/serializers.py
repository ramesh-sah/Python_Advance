from rest_framework import serializers
from .models import Student

# validator level validation

# def starts_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError("Name should start with R")


class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[starts_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    # field level validation

    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError("Seat full")
    #     return value

    # object level validation
    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #     if nm.lower() == 'ram' and ct.lower() != 'ranchi':
    #         raise serializers.ValidationError('city must be ranchi')
    #     return data
