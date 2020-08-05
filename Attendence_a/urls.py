from django.contrib import admin
from django.urls import path
from Attendence_a import views
from django.conf.urls import url
urlpatterns = [
    
    path("signup",views.Signup_teacher_r),
    path("",views.Signup_teacher_r),
    path("teacherlogin",views.Login_teacher),
    path("teacheraccount",views.Teacher_account),
    path('newstudent',views.New_student),
    path('logout',views.logout),
    path('studentlogin',views.Login_student),
    path('studentaccount',views.Student_account),
    path('addsubject',views.Add_subjectt),
    path('addclass',views.Add_classs),
    path('allstudent',views.All_student),
    path('select',views.Select),
    path('mark',views.Mark),
    path('delete/<str:pk>/',views.Delete,name="delete"),
    path('viewattendence',views.Student_view_attendence),
    path('sviewattendence',views.Student_mark_attendence),
]
