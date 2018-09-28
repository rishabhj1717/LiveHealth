from django.shortcuts import render,render_to_response
from django.http import HttpResponse,JsonResponse
from .models import Try,Parent,Department,Courses,Student,Teacher,TeacherResp,Subjects,studMarks,Attendance,Exam,StudentMarks,DailyAttendance
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import logging
from django.core.serializers import serialize
from django.core import serializers
import json
import math
import copy
from datetime import datetime,date
from dateutil import relativedelta
from django.contrib import messages

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
		obj = Department.objects.values('deptName')
		obj1 = Courses.objects.values('courseName')
		jsonmsg1={}
		jsonmsg={}
		arr = []
		arr1=[]
		j=0
		k=0
		for i in obj:
			arr.append(obj[j]['deptName'])
			j=j+1
		#print(arr)
		jsonmsg['departments']=arr
		json_loads = json.dumps(jsonmsg)

		for l in obj1:
			arr1.append(obj1[k]['courseName'])
			k=k+1
		jsonmsg1['courses']=arr1
		json_loads1 = json.dumps(jsonmsg1)	
		context = {
		'jsondept':json_loads,
		'jsoncourse':json_loads1
		}
		print(json_loads1)
		#Try.objects.create(roll=request.POST['roll'],name=request.POST['firstName'])
		return render(request,"studentsignup.html",context)
	elif request.method == "POST" and 'enteacher' in request.POST:

		obj = Department.objects.values('deptName')
		obj1 = Courses.objects.values('courseName')
		jsonmsg1={}
		jsonmsg={}
		arr = []
		arr1=[]
		j=0
		k=0
		for i in obj:
			arr.append(obj[j]['deptName'])
			j=j+1
		#print(arr)
		jsonmsg['departments']=arr
		json_loads = json.dumps(jsonmsg)

		for l in obj1:
			arr1.append(obj1[k]['courseName'])
			k=k+1
		jsonmsg1['courses']=arr1
		json_loads1 = json.dumps(jsonmsg1)	
		context = {
		'jsondept':json_loads,
		'jsoncourse':json_loads1
		}
		print(json_loads1)
		return render(request,"teachersignup.html",context)
	elif request.method == "POST" and 'markupdate' in request.POST:
		return render(request,"updatemarks.html")
	elif request.method == "POST" and 'attupdate' in request.POST:
		obj = Courses.objects.values('courseName')
		jsonmsg1={}
		arr1 = []
		j=0
		for i in obj:
			arr1.append(obj[j]['courseName'])
			j=j+1
		#print(arr)
		jsonmsg1['courses']=arr1
		json_loads = json.dumps(jsonmsg1)
		context = {
		'jsoncourse':json_loads
		}
		print(json_loads)
		return render(request,"atttemp.html",context)
	elif request.method == "POST" and 'deleteStudent' in request.POST:
		return render(request,"delete.html")
	elif request.method == "POST" and 'setexam' in request.POST:
		return render(request,"setexam.html")
	elif request.method == "POST" and 'adddept' in request.POST:
		return render(request,"dept.html")
	elif request.method == "POST" and 'addcourse' in request.POST:
		obj = Department.objects.values('deptName')
		jsonmsg={}
		arr = []
		j=0
		for i in obj:
			arr.append(obj[j]['deptName'])
			j=j+1
		#print(arr)
		jsonmsg['departments']=arr
		json_loads = json.dumps(jsonmsg)
		context = {
		'jsondept':json_loads
		}
		print(json_loads)
		return render(request,"addCourse.html",context)
	elif request.method == "POST" and 'viewAttendance' in request.POST:
		# -- Here the select box has to be done ----------------
		return render(request,"attendenceviewperday.html")
	elif request.method == "POST" and 'addSubjects' in request.POST:
		obj = Department.objects.values('deptName')
		obj1 = Courses.objects.values('courseName')
		jsonmsg1={}
		jsonmsg={}
		arr = []
		arr1=[]
		j=0
		k=0
		for i in obj:
			arr.append(obj[j]['deptName'])
			j=j+1
		#print(arr)
		jsonmsg['departments']=arr
		json_loads = json.dumps(jsonmsg)

		for l in obj1:
			arr1.append(obj1[k]['courseName'])
			k=k+1
		jsonmsg1['courses']=arr1
		json_loads1 = json.dumps(jsonmsg1)	
		context = {
		'jsondept':json_loads,
		'jsoncourse':json_loads1
		}
		print(json_loads1)
		return render(request,'subjectadd.html',context)		



def adminSignup(request):
	if request.method == "POST" and 'login' in request.POST:
		name = request.POST['admin']
		pwd = request.POST['password']
		jsonmsg={}
		if name=='admin' and pwd =='admin':
			jsonmsg['message']='Successful sign in'
			json_loads = json.dumps(jsonmsg)
			context={
			'admin':json_loads
			}

			return render(request,'adminindex.html')
		else:
			jsonmsg['message']='Incorrect Credentials'
			json_loads = json.dumps(jsonmsg)
			context={
			'admin':json_loads
			}
			messages.error(request,'Invalid login credentials')
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
			messages.error(request,'Username already exists. Please try out a new one.')
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
			return render(request,'parentstudentinfo.html',context)
		else:
			messages.error(request,'Invalid Credentials. Please try again')
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
		cid = dept[:1]+course
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
		else:
			cnt1 = Courses.objects.all().count()
			div=chr(cnt1+65)
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
				if StudentMarks.objects.filter(roll=name).exists():
					json_data1 = serializers.serialize('json',StudentMarks.objects.filter(roll=name))
					context={
					'json':json_data,
					'marks':json_data1
					}
				else:
					context={
					'json':json_data,
					'marks':{}
					}
				return render(request,'studentinfo.html',context)
			else:
				messages.error(request,'Invalid login credentials.Retry')
				return render(request,'studentlogin.html')
		else:
			messages.error(request,'Student does not exist.')
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
				messages.error(request,'Invalid Credentials')
				return render(request,'teachersignin.html')
		else:
			messages.error(request,'Teacher does not exist')
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
			div ='A'
		elif cid == 'CPG':
			div ='B'
		elif cid == 'IUG':
			div = 'C'
		elif cid == 'IPG':
			div ='D'

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

#-----------------------------------------------------------------------------------------------

def exam(request):
	if request.method == "POST":
		eid=(Exam.objects.all().count())+1
		sem = request.POST['sem']
		div=request.POST['div']
		subj=request.POST['subject']
		courseid = request.POST['course']
		#today = str(date.today())
		doe = request.POST['date']
		print(doe)
		print(sem)
		doe1=""
		# if sem=='1':
		# 	if Subjects.objects.filter(sem1=subj).exists():
		# 		Exam.objects.create(eid=eid,sem=sem,subj=subj,div=div,doexam=doe,courseId=courseid)
		# 		print("Created Successfully")
		# 		return render(request,'adminindex.html')
		# 	else:
		# 		print("In sem1")
		# 		messages.error(request,'Incorrect Data')
		# 		return render(request,'setexam.html')
		# elif sem=='2':
		# 	if Subjects.objects.filter(sem2=subj).exists():
		# 		Exam.objects.create(eid=eid,sem=sem,subj=subj,div=div,doexam=doe,courseId=courseid)
		# 		print("Created Successfully")
		# 		return render(request,'adminindex.html')
		# 	else:
		# 		messages.error(request,'Incorrect Data')
		# 		return render(request,'setexam.html')
		# elif sem=='3':
		# 	if Subjects.objects.filter(sem3=subj).exists():
		# 		Exam.objects.create(eid=eid,sem=sem,subj=subj,div=div,doexam=doe,courseId=courseid)
		# 		print("Created Successfully")
		# 		return render(request,'adminindex.html')
		# 	else:
		# 		messages.error(request,'Incorrect Data')
		# 		return render(request,'setexam.html')
		# elif sem=='4':
		# 	if Subjects.objects.filter(sem4=subj).exists():
		# 		Exam.objects.create(eid=eid,sem=sem,subj=subj,div=div,doexam=doe,courseId=courseid)
		# 		print("Created Successfully")
		# 		return render(request,'adminindex.html')
		# 	else:
		# 		messages.error(request,'Incorrect Data')
		# 		return render(request,'setexam.html')
		# else:
		# 	messages.error(request,'Incorrect Data')
		Exam.objects.create(eid=eid,sem=sem,subj=subj,div=div,doexam=doe,courseId=courseid)
		d = Exam.objects.filter(eid=eid)
		doe1 = d[0].doexam
		print(doe1)
		print("Created successfully")
		return render(request,'adminindex.html')
	else:
		return render(request,'adminindex.html')

def marksUpdate(request):
	if request.method=='POST':
		roll = request.POST['roll']
		subject=request.POST['subject']
		#doe = request.POST['date']
		doe1 = str(date.today())
		eid=0
		marks = request.POST['marks']
		if Exam.objects.filter(subj=subject).exists():
			obj = Exam.objects.get(subj=subject)
			doexam = obj.doexam
			eid = obj.eid
			print(doexam)
		else:
			messages.error(request,'Exam not set')
			return render(request,'updatemarks.html')

		if StudentMarks.objects.filter(roll=roll,subject=subject).exists():
			d = StudentMarks.objects.get(roll=roll,subject=subject)
			messages.error(request,'Marks already have been updated for the student')
			return render(request,'updatemarks.html')
		else:
			isUpdated=1
			isPresent  =1
			StudentMarks.objects.create(roll=roll,subject=subject,marks=marks,isUpdated=isUpdated,isPresent=isPresent,eid=Exam.objects.get(eid=eid),doexam=doe1)
			return render(request,'adminindex.html')

# def save_events_json(request):
#     if request.is_ajax():
#         if request.method == 'POST':
#             print 'Raw Data: "%s"' % request.body   
#     return HttpResponse("OK")

# 	# function myfunction(){
# 	# var obj={}
# 	# var course = document.getE
	

	# def attendancePerDay(request):
	# 	if request.method == 'POST':
	# 		roll = request.POST['rollno']
	# 		course = 

def attendanceViewPerDay(request):
	if request.method=='POST':
		tod_day = str(date.today())
		isPresent = 0#request.POST['present']
		course = request.POST['course']
		#roll = request.POST['roll']
		subject = request.POST['subject']
		datef = request.POST['datef']
		datet = request.POST['datet']
		

		obj = DailyAttendance.objects.filter(day__range=[datef,datet],course=course,subject=subject)
		jsonarr=[]
		j=0
		for i in obj:
			jsonmsg={}
			jsonmsg['day'] = obj[j].day
			if obj[j].isPresent==1:
				jsonmsg['present'] = 'present'
			else:
				jsonmsg['present'] = 'absent'
			jsonmsg['course']=obj[j].course
			jsonmsg['roll']=obj[j].roll
			jsonmsg['subject']=obj[j].subject
			jsonarr.append(jsonmsg)
			j=j+1

		#json_loads = json.dumps(jsonmsg1)
		# context={
		# 'json':json_loads
		# }
		print(jsonarr)
		return JsonResponse({'json':jsonarr})
	
		# if DailyAttendance.objects.filter(course=course,subject=subject,roll=roll,day=tod_day).exists():
		# 	return JsonResponse({'foo':'bar'})
		# else:
		# 	DailyAttendance.objects.create(day=tod_day,isPresent=isPresent,course=course,roll=roll,subject=subject)
		# cnt = DailyAttendance.objects.filter(roll=roll,subject=subject).count()
		# obj = DailyAttendance.objects.filter(roll=roll,subject=subject)
		# attlec=0
		# for i in obj:
		# 	if i.isPresent==1:
		# 		attlec = attlec+1
		# print(attlec/cnt)

def attendancePerDay(request):
	if request.method=='POST':
		tod_day = str(date.today())
		print(tod_day)
		isPresent = request.POST['present']
		course = request.POST['course']
		roll = request.POST['rollno']
		subject = request.POST['subject']
		div=""
		if DailyAttendance.objects.filter(course=course,subject=subject,roll=roll,day=tod_day).exists():
			messages.error(request,'Attendance has been taken')
			obj = Courses.objects.values('courseName')
			jsonmsg1={}
			arr1 = []
			j=0
			for i in obj:
				arr1.append(obj[j]['courseName'])
				j=j+1
			#print(arr)
			jsonmsg1['courses']=arr1
			json_loads = json.dumps(jsonmsg1)
			context = {
			'jsoncourse':json_loads
			}
			print(json_loads)
			return render(request,'atttemp.html',context)
		else:
			DailyAttendance.objects.create(day=tod_day,isPresent=isPresent,course=course,roll=roll,subject=subject)
		cnt = DailyAttendance.objects.filter(roll=roll,subject=subject).count()
		obj = DailyAttendance.objects.filter(roll=roll,subject=subject)
		attlec=0
		for i in obj:
			if i.isPresent==1:
				attlec = attlec+1
		cnt1 = DailyAttendance.objects.filter(roll=roll,isPresent=1).count()
		cnt2 = DailyAttendance.objects.filter(roll=roll).count()
		att = (cnt1/cnt2)*100
		print(att)
		d = Student.objects.get(roll_id=roll)
		d.attendance=att
		d.save()
		print('successfully updated the attendance')
		return render(request,'adminindex.html')
	# elif request.method=='POST' and 'cancel' in request.POST:
	# 	return render(request,'adminindex.html')
		# if Student.objects.filter(roll_id=roll,course=course).exists():
		# 	print ("In here")
		# 	obj = Student.objects.get(roll_id=roll,course=course)
		# 	obj.attendance = att;
		# 	obj.save()
		# 	context={
		# 	'message':'attendance updated successfully'
		# 	}
		# 	return render(request,'adminindex.html',context)
		# else:
		# 	jsonmsg={}
		# 	jsonmsg['message']='Incorrect Details'
		# 	json_loads = json.dumps(jsonmsg)
		# 	context={
		# 	'json':json_loads
		# 	}
		# 	return render(request,'atttemp.html',context) 
		
		# flag = updateAtt(lecId,roll,cnt,attlec,div)
		# if flag==0:
		# 	context={
		# 	'message':'Something went wrong'
		# 	}
		# 	return render(request,'atttemp.html',context)
		# else:
		# 	context={
		# 	'message':'Attendance Updated successfully'
		# 	}
		# 	return render(request,'adminindex.html',context)

# def updateAtt(lecId,roll,cnt,attlec,div):

# 	roll1 = roll
# 	eid = lecId
# 	tot_lec = cnt
# 	att_lec = attlec
# 	r = Student.objects.filter(div=div)
# 	for i in r:
# 		roll = i.roll_id
# 		if Attendance.objects.filter(lecId=eid,roll=roll).exists():
# 			return 0
# 		else:
# 			Attendance.objects.create(lecId=eid,roll=roll)


# 	# 	# calcAttendance(eid,roll1)
# 	if Attendance.objects.filter(lecId=eid,roll=roll1).exists():
# 		obj = Attendance.objects.get(lecId=eid,roll=roll1)
# 		calcatt = (int(att_lec)/int(tot_lec))*100
# 		print(calcatt)
# 		obj.curratt = calcatt
# 		obj.save()
# 	else:
# 		return 0

# 	data = Attendance.objects.filter(roll=roll1)
# 	avg=0
# 	tempatt=0
# 	for k in data:
# 		tempatt =tempatt+ k.curratt
# 		avg = avg+1
# 		resatt = tempatt/avg
# 		data1 = Student.objects.get(roll_id=roll1)
# 		data1.attendance = resatt
# 		data1.save()
		
# 	return 1
	
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

	


def addDepartment(request):
	if request.method == "POST":
		obj = request.POST
		deptName = obj['dept']
		deptObj = Department.objects.all()
		cnt = Department.objects.all().count()
		jsonmsg = {}
		if Department.objects.filter(deptName=deptName).exists():
			jsonmsg['isPresent']=0
			jsonmsg['message']='Department already exists'
			json_data = json.dumps(jsonmsg)
			context = {
			"json":json_data
			}
			print(context)
			messages.error(request,'Department already exists')
			return render(request,'dept.html',context)
		else:
			jsonmsg['isPresent']=1
			jsonmsg['message']='Successfull'
			json_data = json.dumps(jsonmsg)
			context = {
			"json":json_data
			}
			print(context)
			Department.objects.create(deptId=cnt+1,deptName=deptName)
			return render(request,'adminindex.html',context)

def addCourse(request):
	if request.method == "POST":
		obj = request.POST
		deptName = obj['dept']
		courseName = obj['course']
		courseName = deptName[0]+courseName
		sem = 4
		jsonmsg = {}
		if Courses.objects.filter(deptName=deptName,courseName=courseName).exists():
			jsonmsg['isPresent']=0
			jsonmsg['message']='Course Already exists'
			json_data = json.dumps(jsonmsg)
			# context = {
			# "json":json_data
			# }


			obj = Department.objects.values('deptName')
			jsonmsg1={}
			arr = []
			j=0
			for i in obj:
				arr.append(obj[j]['deptName'])
				j=j+1
		#print(arr)
			jsonmsg1['departments']=arr
			json_loads = json.dumps(jsonmsg)
			context = {
			'json':json_data,
			'jsondept':json_loads
			}
			print(json_loads)

			
			return render(request,'adminindex.html',context)
		else:
			jsonmsg['isPresent']=1
			jsonmsg['message']='Successful'
			json_data = json.dumps(jsonmsg)
			context = {
			"json":json_data
			}
			Courses.objects.create(courseName=courseName,deptName=Department.objects.get(deptName=deptName),sem=sem)
			return render(request,'adminindex.html',context)

def addSubject(request):
	if request.method == 'POST' and 'submit' in request.POST:
		obj = request.POST
		dept = obj['dept']
		course = obj['course']
		subj1 = obj['subj1']
		subj2 = obj['subj2']
		subj3 = obj['subj3']
		subj4 = obj['subj4']
		subj5 = obj['subj5']
		subj6 = obj['subj6']
		subj7 = obj['subj7']
		subj8 = obj['subj8']
		a = insertSubject(subj1,subj3,subj5,subj7,course,dept)
		a = insertSubject(subj2,subj4,subj6,subj8,course,dept)
		if a==1:
			messages.success(request,'Subjects entered successfully')
			return render(request,'adminindex.html',{'message':'Save complete'})
		else:
			messages.error(request,'Something went wrong')
			obj = Department.objects.values('deptName')
			obj1 = Courses.objects.values('courseName')
			jsonmsg1={}
			jsonmsg={}
			arr = []
			arr1=[]
			j=0
			k=0
			for i in obj:
				arr.append(obj[j]['deptName'])
				j=j+1
			#print(arr)
			jsonmsg['departments']=arr
			json_loads = json.dumps(jsonmsg)
	
			for l in obj1:
				arr1.append(obj1[k]['courseName'])
				k=k+1
			jsonmsg1['courses']=arr1
			json_loads1 = json.dumps(jsonmsg1)	
			context = {
			'jsondept':json_loads,
			'jsoncourse':json_loads1
			}
			print(json_loads1)
			return render(request,'subjectadd.html',context)
	elif request.method == 'POST' and 'cancel' in request.POST:
		return render(request,'adminindex.html')


def insertSubject(subj1,subj2,subj3,subj4,course,dept):
	Subjects.objects.create(sem1=subj1,sem2=subj2,sem3=subj3,sem4=subj4,courseName=Courses.objects.get(courseName=course),deptName=Department.objects.get(deptName=dept))
	return 1

		


