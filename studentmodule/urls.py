from django.urls import path

from . import views



urlpatterns = [
	path('', views.home, name='student-module-home'), 
	path('admin_login/', views.admin_login , name='student-module-admin_login'),
	path('student_login/', views.student_login , name='student-module-student_login'),
	path('student_signup/',views.student_signup,name='student-module-student_signup'),
	path('screen2/',views.screen2,name='student-module-screen2'),
	path('choosefile/',views.choosefile,name='student-module-choosefile')

	#path('student_login/student_signup/',views.student_signup,name='student-module-student_signup'),
	
]
