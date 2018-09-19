from django.shortcuts import render
from django.http import HttpResponse
from .models import Try,Parent,Department,Courses,Student,Teacher,TeacherResp,Subjects,studMarks,Attendance
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import logging
from django.core.serializers import serialize
from django.core import serializers
import json
from django.http import JsonResponse 
import math
from datetime import datetime,date
from dateutil import relativedelta

divchar = ord('A')

logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
	return render(request,'index.html')

def detail(request):
	if request.method == "POST" and 'admin' in request.POST:
		#Try.objects.create(roll=request.POST['roll'],name=request.POST['firstName'])
		return render(request,"adminsignup.html")
	elif request.method == "POST" and 'student' in request.POST:
			#Try.objects.create(roll=request.POST['roll'],name=request.POST['firstName'])
		return render(request,"studentlogin.html")
	elif request.method == "POST" and 'teacher' in request.POST:
		return render(request,"teachersignin.html")
	elif request.method == "POST" and 'parent' in request.POST:
		return render(request,"home.html")
	# elif request.method == "POST" and 'deleteStudent' in request.POST:
	# 	return render(request,"delete.html")


def adminControl(request):
	if request.method == "POST" and 'enstudent' in request.POST:
		#Try.objects.create(roll=request.POST['roll'],name=request.POST['firstName'])
		return render(request,"studentsignup.html")
	elif request.method == "POST" and 'enteacher' in request.POST:

		#json_data = {"comp":1,"IT":2}
		#data = Subjects.objects.filter(courseName='CUG')
		json_data = serializers.serialize('json',Subjects.objects.all())
		context = {
		"json":json_data
		}
		return render(request,"teachersignup.html",context)
	elif request.method == "POST" and 'markupdate' in request.POST:
		return render(request,"marks.html")
	elif request.method == "POST" and 'attupdate' in request.POST:
		return render(request,"att1.html")
	elif request.method == "POST" and 'deleteStudent' in request.POST:
		return render(request,"delete.html")
	elif request.method == "POST" and 'setexam' in request.POST:
		return render(request,"setexam.html")




def adminSignup(request):
	if request.method == "POST" and 'login' in request.POST:
		name = request.POST['admin']
		pwd = request.POST['password']

		if name=='admin' and pwd =='admin':
			return render(request,'adminindex.html')
		else:
			return render(request,'adminsignup.html')

	elif request.method == "POST" and 'cancel' in request.POST:
		return render(request,'index.html')



#-------------------------------------------------------------------------------------------------
#--------------------------This is parent signup and login--------------------------------------------------

def parControl(request):
	if request.method == "POST" and 'signup' in request.POST:
		return render(request,'signup.html')
	elif request.method == "POST" and 'login' in request.POST:
		return render(request,'login.html')


def signup(request):
	if request.method == "POST" and 'signup' in request.POST:
		if Parent.objects.filter(puname=request.POST['uname']).exists():
			return render(request,'signup.html',{'message':'username already exists'})
		else:
			user = User.objects.create_user(username=request.POST['uname'],password=request.POST['pwd'])
			Parent.objects.create(name=request.POST["name"],phone=request.POST["phone"],emailP=request.POST["email"],address=request.POST["address"],puname=request.POST["uname"],pwd=request.POST["pwd"])
			return render(request,'home.html')	
	else:
		return render(request,'index.html')
		
def log_in(request):
	if request.method == "POST":
		username = request.POST['uname']
		pwd = request.POST['pwd']
		user = authenticate(username = username, password = pwd)
		if user is not None:
			data = Parent.objects.get(puname=username)
			id = data.puname
			data1 = Student.objects.filter(puname=id)
			data2 = Parent.objects.filter(puname=username) 
			json_data = serializers.serialize('json',data1)
			json_data2 = serializers.serialize('json',data2)
			context = {
			"json":json_data,
			"parent":json_data2,
			}
			return render(request,'parentinfo.html',context)
		else:
			return render(request,'login.html',{'message':'incorrect password or username'})


#-----------------------------------------------Admin subject and department code------------------------

def deptinfo(request):
	if request.method == "GET":
		# Department.objects.create(deptId=request.POST["deptid1"],deptName=request.POST["dept1"])
		# Department.objects.create(deptId = request.POST["deptid2"], deptName=request.POST["dept2"])
		# data = Teacher.objects.get(teacherId='TCPG1')
		# id = data.teacherId
		# data1 = TeacherResp.objects.filter(teacher = id)

		data = Parent.objects.get(puname='rishb')
		id = data.puname
		data1 = Student.objects.filter(puname=id)
		data2 = Parent.objects.filter(puname='rishb') 

		json_data = serializers.serialize('json',data1)
		json_data2 = serializers.serialize('json',data2)
		context = {
		"json":json_data,
		"parent":json_data2,
		}
		#return HttpResponse(json_data)
		return render(request,'json.html',context)
	else:
		return HttpResponse('<h2>It does not work</h2>')		
#-------------------------------------------------Leave this code for the time being----------------------
def courses_subjects(request):
	if request.method == "POST":
		dept1 = request.POST['dept1']
		course1 = request.POST['course1']
		course2 = request.POST['course2']

		dept2 = request.POST['dept2']
		course3 = request.POST['course3']
		course4 = request.POST['course4']

		pre = dept1[:2]
		course11 = pre+course1
		course22 = pre+course2

		pre = dept2[:2]
		course33 = pre+course3
		course43 = pre+course4

		#Courses.objects.create(courseName = )

		print(pre)
		return HttpResponse('<h1>It works</h1>')

#-----------------------------------------------------------------------------------

def studentSignup(request):
	if request.method == "POST" and 'signup' in request.POST:
		name = request.POST['name']
		phone = request.POST['phone']
		email = request.POST['email']
		address = request.POST['address']
		dept = request.POST['dept']
		course = request.POST['course']
		doj = '2018-06-01'
		puname = request.POST['puname']
		cnt = Student.objects.filter(dept = dept,course=course).count()
	#print(cnt)
		cnt=cnt+1
		roll = dept[:1]+course+str(cnt)
	#print(roll)
		print(doj)
		today = str(date.today())
		date2 = datetime.strptime(str(today),'%Y-%m-%d')
		date1 = datetime.strptime(str(doj), '%Y-%m-%d')
		r = relativedelta.relativedelta(date2,date1)
		m = abs(r.months)
		print(m)
		sem=(m/6)+1
		if 'CUG' in roll:
			div='A'
		elif 'CPG' in roll:
			div='B'
		elif 'IUG' in roll:
			div='C'
		elif 'IPG' in roll:
			div='D'
		Student.objects.create(name=name,phone=phone,emailP=email,address=address,dept=dept,course=course,doj=doj,puname_id=puname,attendance=0,div=div,roll_id=roll,sem=1)
		return render(request,'adminindex.html',{'message':'successful entry'})
	elif request.method == 'POST' and 'cancel' in request.POST:
		return render(request,'studentsignup.html')


def studentLogin(request):
	if request.method == "POST" and 'signin' in request.POST:
		name = request.POST['name']
		password = request.POST['password']
		if Student.objects.filter(roll_id=name).exists():
			if name == password:
				#data = Student.objects.get(name)
				json_data = serializers.serialize('json',Student.objects.filter(roll_id=name))
				json_data1 = serializers.serialize('json',studMarks.objects.filter(roll=name))
				context={
				'json':json_data,
				'marks':json_data1
				}
				return render(request,'studentinfo.html',context)
			else:
				return render(request,'studentlogin.html')
		else:
			return render(request,'studentlogin.html')
	elif request.method == "POST" and 'cancel' in request.POST:
		return render(request,'index.html')

	else:
		return render(request,'index.html')

#--------------------------------------------------------------------------------------------

def markAttendance(request):
	if request.method == "POST":
		roll = request.POST['roll']
		att_lec = request.POST['lecatt']
		tot_lec = request.POST['totatt']
		attendance = (int(att_lec)/int(tot_lec))*100
		print(attendance)
		try:
			t= Student.objects.get(roll_id=roll)
		except Student.DoesNotExist:
			t=None
		if t!=None:
			t.attendance=attendance
			t.save()
			return render(request,'adminindex.html')
		else:
			return render(request,'attendance.html',{'message':'Wrong inputs'})
	else:
		return render(request,'adminindex.html')
#-------------------------------------To be written with teacher login logic------------------
# def marksPercentage(request):
# 	roll='CUG1'

def registerTeacher(request):
 	
	if request.method == "POST" and 'signup' in request.POST:
		name = request.POST['name']
		dept = request.POST['dept']
		course = request.POST['course']
		sem = request.POST['sem']
		subj = request.POST['subject']
		div = request.POST['div']

		cnt = TeacherResp.objects.all().count()
		cnt=cnt+1
		cnt1 = Teacher.objects.all().count()
		id = 'T'+dept[:1]+course+str(cnt1+1)
		if Teacher.objects.filter(teacherId=id).exists():
			TeacherResp.objects.create(id=cnt,dept=dept,course=course,sem=sem,subj=subj,div=div,isExam=0,teacher=Teacher.objects.get(teacherId=id))
			print("Should work")
		else:
			Teacher.objects.create(teacherId = id, teacher_name=name)
			TeacherResp.objects.create(id=cnt,dept=dept,course=course,sem=sem,subj=subj,div=div,isExam=0,teacher=Teacher.objects.get(teacherId=id))
			print("works hopefully")

	return render(request,'adminindex.html')


def teacherLogin(request):
	if request.method == "POST" and 'signin' in request.POST:
		name = request.POST['name']
		password = request.POST['password']
		if Teacher.objects.filter(teacherId=name).exists():
			if name == password:
				json_data = serializers.serialize('json',Teacher.objects.filter(teacherId=name))
				json_data1 = serializers.serialize('json',TeacherResp.objects.filter(teacher=Teacher.objects.get(teacherId=name)))
				context = {
				"teacherName":json_data,
				"json":json_data1
				}
				return render(request,'teacherinfo.html',context)
			else:
				return render(request,'teachersignin.html')
		else:
			return render(request,'teachersignin.html')
	elif request.method == "POST" and 'cancel' in request.POST:
		return render(request,'index.html')

	else:
		return render(request,'index.html')

#---------------------------------------------------------------------------------------------

def updateMarks(request):
	if request.method == "POST":
		roll = request.POST['roll']
		marks = request.POST['marks']
		cid = request.POST['course']
		sid = request.POST['sem']
		# sem = "sem"+sid
		sub = request.POST['subject']
		#print(r1 + " "+m1)
		eid = cid+sid+sub
		try:
			stud = studMarks.objects.get(roll=roll,examid=eid)
		except studMarks.DoesNotExist:
			stud = None

		if stud != None:
			stud.marks = marks
			stud.save()
			return render(request,'adminindex.html')
		else:
			# context = {
			# "json":{'message':'Incorrect rollno or marks format'},
			# }
			return render(request,'marks.html')
	else:
		return render(request,'adminindex.html')


#--------------------------------------Delete Student------------------------------------------

def deleteStudent(request):
	if request.method == 'POST' and 'submit' in request.POST:
		roll = request.POST['roll']
		try:
			d = Student.objects.get(roll_id=roll)
		except Student.DoesNotExist:
			d=None

		if d!=None:
			d.delete()
		
		return render(request,'adminindex.html')
	else:
		return render(request,'index.html')

def setExam(request):
	if request.method == 'POST' and 'submit' in request.POST:
		cid = request.POST['course']
		sid = request.POST['sem']
		sem = "sem"+sid
		sub = request.POST['subject']
		eid=""
		div=""
		if Subjects.objects.filter(courseName=cid):
			d=Subjects.objects.filter(courseName=cid)
		else:
			return render(request,'adminindex.html')
		pdata = serializers.serialize('python',d)
		#dd = json.loads(json.dumps(json_data))
		j=0
		for i in pdata:

			if pdata[j]['fields'][sem] == sub:
				eid = cid+sid+sub
				break
			else:
				j=j+1
		if eid=="":
			return render(request,'adminindex.html')
		print(eid)
		if cid == 'CUG':
			div='A'
		elif cid=='CPG':
			div='B'
		elif cid=='IUG':
			div='C'
		elif cid=='IPG':
			div='D'

		r = Student.objects.filter(div=div)
		for i in r:
			roll = i.roll_id
			studMarks.objects.create(examid=eid,roll_id=roll)
		return render(request,'adminindex.html')
	elif request.method == 'POST' and 'cancel' in request.POST:
		return render(request,'setexam.html')
	else:
		return render(request,'index.html')


def markingAtt(request):
	if request.method == 'POST': #and 'submit' in request.POST:
		tid = request.POST['teacher']
		sid = tid[1:4]
		roll1 = request.POST['roll']
		tot_lec = request.POST['totatt']
		att_lec = request.POST['lecatt']
		sub = request.POST['subject']

		print(tid+" "+sid+" "+roll1)
	#sub='Electronics'
		eid=""
		div=""
		# if int(att_lec)<int(tot_lec):
		#  	return HttpResponse('<h1>Error at the start</h1>')
			#return render(request,'att1.html')
		try:
			t=Teacher.objects.get(teacherId=tid)
		except Teacher.DoesNotExist:
			t=None
	#print(t.teacherId)
		if t==None:
			return HttpResponse("<h1>Error at Teacher does not exist</h1>")
			#return render(request,'att1.html')
		else:
			d = TeacherResp.objects.filter(teacher=Teacher.objects.get(teacherId=tid))
			pdata = serializers.serialize('python',d)
			j=0

			for i in pdata:
				if pdata[j]['fields']['subj']==sub:
					div = pdata[j]['fields']['div']
					eid=sub+div+sid
					print(eid)
					break
				else:
					j=j+1
			if eid=="":
				return render(request,'att1.html')
			r = Student.objects.filter(div=div)
			for i in r:
				roll = i.roll_id
				if Attendance.objects.filter(lecId=eid,roll=roll).exists():
					print("Does not matter")
				else:
					Attendance.objects.create(lecId=eid,roll=roll)


		# calcAttendance(eid,roll1)
			if Attendance.objects.filter(lecId=eid,roll=roll1):
				obj = Attendance.objects.get(lecId=eid,roll=roll1)
				calcatt = (int(att_lec)/int(tot_lec))*100
				print(calcatt)
				obj.curratt = calcatt
				obj.save()
			else:
				return HttpResponse('<h1>Problem Here</h1>')

			data = Attendance.objects.filter(roll=roll1)
			avg=0
			tempatt=0
			for k in data:
				tempatt =tempatt+ k.curratt
				avg = avg+1
			resatt = tempatt/avg
			data1 = Student.objects.get(roll_id=roll1)
			data1.attendance = resatt
			data1.save()
		
		return render(request,'index.html')
	else:

		return render(request,'index.html')
# def calcAttendance(prid,rollno):
# 	calcatt=0
# 	if Attendance.objects.filter(lecId=prid,roll=rollno):
# 			obj = Attendance.objects.get(lecId=eid,roll=roll1)
# 			calcatt = (att_lec/tot_lec)*100
# 			print(calcatt)
# 			obj.curratt = calcatt
# 			obj.save()
# 	else:
# 		return render(request,'att1.html')
# 	return

