from django.shortcuts import render
from django.http import HttpResponse
from .models import Try,Parent
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# Create your views here.
def index(request):
	return render(request,'home.html')

def detail(request):
	if request.method == "POST" and 'signup' in request.POST:
		#Try.objects.create(roll=request.POST['roll'],name=request.POST['firstName'])
		return render(request,"signup.html")
	else:
		if request.method == "POST" and 'login' in request.POST:
			#Try.objects.create(roll=request.POST['roll'],name=request.POST['firstName'])
			return render(request,"try1.html")
#-------------------------------------------------------------------------------------------------
#--------------------------This is parent signup and login--------------------------------------------------

def signup(request):
	if request.method == "POST" and 'signup' in request.POST:
		if Parent.objects.filter(puname=request.POST['uname']).exists():
			return render(request,'signup.html',{'message':'username already exists'})
		else:
			user = User.objects.create_user(username=request.POST['uname'],password=request.POST['pwd'])
			Parent.objects.create(name=request.POST["name"],emailP=request.POST["email"],address=request.POST["address"],puname=request.POST["uname"],pwd=request.POST["pwd"])
			return render(request,'login.html')	
		
def log_in(request):
	if request.method == "POST":
		username = request.POST['uname']
		pwd = request.POST['pwd']
		user = authenticate(username = username, password = pwd)
		if user is not None:
			return HttpResponse('<h1>Parent can login and will be registering his children </h1>')
		else:
			return render(request,'login.html',{'message':'incorrect password or username'})



