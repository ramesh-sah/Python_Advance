from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value

    class Meta:
        model = Student
        fields = '__all__'
