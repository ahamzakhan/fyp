from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import student_info
from django.contrib.auth.models import User, auth


def home(request):
	return render(request,'studentmodule/home.html')
	
def choosefile(request):
	return render(request,'studentmodule/choosefile.html')

def screen2(request):
	return render(request,'studentmodule/s2.html')


def admin_login(request):

	if request.method == 'POST':
		username= request.POST['username']
		password= request.POST['psw']

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return render(request,'studentmodule/choosefile.html')
		else:
			return render(request,'studentmodule/admin_login.html')

	else:
		return render(request,'studentmodule/admin_login.html')



def student_signup(request):
	if request.method == 'POST':	
		roll_no = request.POST["roll_no"]
		emailAdress = request.POST["emailAddress"]
		password = request.POST["password"]
		verification = request.POST["verification"]
		campus_name = request.POST["campus_name"]
		s_info = student_info(roll_no=roll_no,mail=emailAdress,password=password, city=campus_name)
		s_info.save()
		return render(request,'studentmodule/student_login.html')
	else:
		return render(request,'studentmodule/signup.html')

def student_login(request):
	if request.method == 'POST':
		roll_no = request.POST['roll_no']
		password=request.POST['psw']
		s_info= student_info.objects.get(roll_no=roll_no)

		if s_info.roll_no == roll_no and s_info.password == password:
			return render(request,'studentmodule/s1.html')
		else:
			return render(request,'studentmodule/student_login.html')	
	else:
		return render(request,'studentmodule/student_login.html')

	