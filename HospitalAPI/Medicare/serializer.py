from rest_framework import serializers
from .models import Users,Hospital,BookAppointment,DoctorReview,ImageUpload

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ['id','title','image','uploaded_at']

class BookAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= BookAppointment
        fields = '__all__'

class DoctorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorReview
        fields ='__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        username = serializers.CharField()
        password = serializers.CharField()
        model = Users
        fields = ['name','username','password']