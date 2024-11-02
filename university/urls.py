from django.urls import path
from university.views import *


urlpatterns = [
    path('students/', StudentListView.as_view(), name='students'),
    path('students/<int:id>/', StudentDetailView.as_view(), name='student_info'),
    path('students/<int:id>/delete/', DeleteStudentView.as_view(), name='remove_student'),
    path('students/<int:id>/update/', EditStudentView.as_view(), name='edit_student'),
    path('add_student/', CreateStudentView.as_view(), name='add_student')




]