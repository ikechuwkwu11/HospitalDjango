from django.core.serializers import serialize
from rest_framework.views import APIView
from.serializer import HospitalSerializer,RegistrationSerializer,LoginSerializer,BookAppointmentSerializer,DoctorReviewSerializer,ImageUploadSerializer
from .models import Hospital,BookAppointment,DoctorReview,ImageUpload
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
# Create your views here.


class Register(APIView):
    def post(self,request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have been registered. Thank you!!'},status=200)
            return Response({'message':'Registration Failed. Try again!'},status=400)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=500)


class Login(APIView):
    def post(self,request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response({'message':'You have been logged in'},status=200)
            return Response({'message': 'Invalid login data'}, status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class Logout(APIView):
    def get(self,request):
        try:
            logout(request)
            return Response({'message':'You have successfully logged out'},status=200)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class AddHospital(APIView):
    def post(self,request):
        try:
            serializer = HospitalSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully added hospital'},status=200)
            return Response({serializer.errors},status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class HospitalList(APIView):
    def get(self,request):
        try:
            hospital = Hospital.objects.all()
            serializer = HospitalSerializer(hospital,many=True)
            return Response(serializer.data,status=200)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class HospitalSingle(APIView):
    def get(self,request,hospital_id):
        try:
            hospital = Hospital.objects.get(id=hospital_id)
            serializer = HospitalSerializer(hospital)
            return Response(serializer.data,status=200)
        except Hospital.DoesNotExist:
            return Response({'message':'This hospital does not exist'})
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class ImageUploadView(APIView):
    def post(self,request):
        try:
            serializer = ImageUploadSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=201)
            return Response(serializer.errors,status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

    def get(self,request):
        images = ImageUpload.objects.all()
        serializer = ImageUploadSerializer(images, many=True)
        return Response(serializer.data,status=200)


class AddBookAppointment(APIView):
    def post(self,request):
        try:
            serializer = BookAppointmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have booked an appointment with the doctor'},status=200)
            return Response({'message':'Appointment not booked, please try again'},status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class BookAppointment_all(APIView):
    def get(self,request):
        try:
            appointment = BookAppointment.objects.all()
            serializer = BookAppointmentSerializer(appointment,many=True)
            return Response(serializer.data,status=200)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class BookAppointment_single(APIView):
    def get(self,request,booking_id):
        try:
            appointment=BookAppointment.objects.get(id = booking_id)
            serializer = BookAppointmentSerializer(appointment)
            return Response(serializer.data,status=200)
        except BookAppointment.DoesNotExist:
            return Response({'message':'This Id does not exist.. Please try again'},status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class BookAppointment_edit(APIView):
    def put(self,request,booking_id):
        try:
            appointment = BookAppointment.objects.get(id=booking_id)
            serializer = BookAppointmentSerializer(appointment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully edited'},status=200)
            return Response({'message':'Please fill in all'},status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)


class DeleteAppointment(APIView):
    def delete(self,request,booking_id):
        try:
            appointment = BookAppointment.objects.get(id=booking_id)
            appointment.delete()
            return Response({'message':'Your booking has been deleted'},status=200)
        except BookAppointment.DoesNotExist:
            return Response({'message':'This booking does not exist'},status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)


class AddDoctorReview(APIView):
    def post(self,request):
        try:
            serializer = DoctorReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your review has been added'},status=200)
            return Response({'message':'Your review was not added'},status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)


class DoctorReview(APIView):
    def get(self,request,review_id):
        try:
            review = DoctorReview.object.get(id=review_id)
            serializer = DoctorReviewSerializer(review)
            return Response(serializer.data,status=200)
        except DoctorReview.DoesNotExist:
            return Response({'message':'Your doctor review not found or has not been done yet. Please try again later. Thank you'})
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class DoctorReviewEdit(APIView):
    def put(self,request,review_id):
        try:
            review = DoctorReview.objects.get(id=review_id)
            serializer = DoctorReviewSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have edited your doctor review'},status=201)
            return Response({'message':'doctor review not changed'},status=400)
        except DoctorReview.DoesNotExist:
            return Response({'message':'doctor review not found'},status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)



