from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    specialized = models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)

class ImageUpload(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/', max_length=300)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class BookAppointment(models.Model):
    name = models.CharField(max_length=100)
    hospital_id = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class DoctorReview(models.Model):
    name = models.CharField(max_length=200)
    review = models.CharField(max_length=200)
    drugs = models.CharField(max_length=200)
    injections = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)