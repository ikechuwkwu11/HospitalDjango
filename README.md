# 🏥 Hospital Management System API (Django REST Framework)
This is a RESTful API built with Django and Django REST Framework (DRF) to manage hospitals, doctor appointments, user authentication, image uploads, and doctor reviews. It serves as a powerful backend for healthcare or hospital-related web/mobile applications.

## 🚀 Features
👤 User Authentication
- Register a new user
- Login and receive authentication credentials
- Logout to end session

🏥 Hospital Management
- Add new hospitals
- View all hospitals
- View details of a single hospital

📅 Appointments
- Book a doctor appointment
- View all appointments
- View details of a specific appointment
- Edit existing appointments
- Delete appointments

🖼️ Image Uploads
- Upload hospital or doctor-related images
- View a list of uploaded images

⭐ Doctor Reviews
- Add a review for a doctor
- View individual reviews
- Edit existing reviews

## 🧱 Technologies Used
- Purpose	Technology
- Backend Framework	Python, Django
- API Development	Django REST Framework (DRF)
- Authentication	Django's built-in User model
- Database	SQLite (can be replaced)
- Image Handling	Django FileField/ImageField

You can test the API using tools such as:
- Postman
- curl
- httpie

## 📌 Future Improvements
- Role-based access control (admin, doctor, patient)
- JWT authentication
- Integration with external health APIs
- Email notifications for appointment confirmations
