from django.urls import path
from .views import Register,Login,AddHospital,HospitalList,HospitalSingle,ImageUploadView,AddBookAppointment,BookAppointment_all,BookAppointment_single,BookAppointment_edit,DeleteAppointment,AddDoctorReview,DoctorReview,DoctorReviewEdit

urlpatterns= [
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('add-hospital/',AddHospital.as_view(),name='add-hospital'),
    path('hospital-list/',HospitalList.as_view(),name='hospital-list'),
    path('hospital-single/',HospitalSingle.as_view(),name='hospital-single'),
    path('image/',ImageUploadView.as_view(),name='image'),
    path('add-book-appointment/',AddBookAppointment.as_view(),name='add-book-appointment'),
    path('book-appointment-all/',BookAppointment_all.as_view(),name='book-appointment-all'),
    path('book-appointment-single/<int:booking_id>',BookAppointment_single.as_view(),name='book-appointment-single'),
    path('book-appointment-edit/<int:booking_id>',BookAppointment_edit.as_view(),name='book-appointment-edit'),
    path('delete-appointment/<int:booking_id>',DeleteAppointment.as_view(),name='delete-appointment'),
    path('add-doctor-review/',AddDoctorReview.as_view(),name='add-doctor-review'),
    path('doctor-review/<int:review_id>',DoctorReview.as_view(),name='doctor-review'),
    path('doctor-review-edit/<int:review_id>',DoctorReviewEdit.as_view(),name='doctor-review-edit')
]
