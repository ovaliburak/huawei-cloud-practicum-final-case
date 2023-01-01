from rest_framework import serializers
from job.models import JobApplication
class JobSerializer(serializers.Serializer):
    resume = serializers.ImageField()
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    phone_number = serializers.CharField()
    email=serializers.EmailField()

    class Meta:
        fields= '__all__'

    def create(self,validated_data):
        return JobApplication.objects.create(**validated_data)
