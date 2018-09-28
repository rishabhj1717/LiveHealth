from django.urls import path,re_path
from django.conf.urls import url,include

from . import views
app_name = 'webapp'
urlpatterns = [
	url(r'^$',views.index,name="index"),
	url(r'^adminsignin$',views.adminSignup),
	url(r'^home$',views.detail),
	url(r'^adminindex$',views.adminControl),
	url(r'^signup$',views.signup),
	url(r'^studentsignup$',views.studentSignup),
	url(r'^studentlogin$',views.studentLogin),
	url(r'^teachersignup',views.registerTeacher),
	url(r'^teachersignin$',views.teacherLogin),
	url(r'^marks$',views.updateMarks),
	url(r'^attendance$',views.markAttendance),
	url(r'^login$',views.log_in),
	url(r'^dept$',views.addDepartment),
	url(r'^courses$',views.courses_subjects),
	url(r'^parent$',views.parControl),
	url(r'^deleteStudent$',views.deleteStudent),
	url(r'^setexam$',views.exam),
	url(r'^attendance1$',views.markingAtt),
	url(r'^addcourses$',views.addCourse),
	url(r'^atttest$',views.attendanceViewPerDay),
	url(r'^try$',views.attendancePerDay),
	url(r'^addsubject$',views.addSubject),
]