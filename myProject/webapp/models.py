from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Try(models.Model):
	roll = models.IntegerField(default = 0)
	name = models.CharField(max_length=100,blank=False,null=False)

class Parent(models.Model):
	name = models.CharField(max_length=100,blank=False,null=False)
	phone  = models.CharField('Phone number', max_length=10, validators=[MinLengthValidator(10)])
	emailP = models.EmailField(max_length=100)
	address = models.CharField(max_length=1000)
	puname = models.CharField(max_length=10,primary_key=True)
	pwd = models.CharField(max_length=100)

class Student(models.Model):
	roll_id = models.CharField(max_length=10,primary_key=True,default='CUG1')
	name = models.CharField(max_length=100,blank=False,null=False)
	phone  = models.CharField('Phone number', max_length=10, validators=[MinLengthValidator(10)])
	emailP = models.EmailField(max_length=100)
	address = models.CharField(max_length=1000)
	dept = models.CharField(max_length=50)
	course = models.CharField(max_length=50)
	doj = models.DateField()
	puname = models.ForeignKey(Parent,on_delete = models.CASCADE, default='0')
	sem = models.IntegerField(default=1,blank=False,null=False)
	div = models.CharField(max_length=2,default='A')
	#marks = models.IntegerField(default=0,blank=True,null=True)
	attendance = models.DecimalField(decimal_places=2,max_digits=5, default = 0)


class Department(models.Model):
	deptId = models.IntegerField(default=0)
	deptName = models.CharField(max_length=100, primary_key=True)

class Courses(models.Model):
	deptName = models.ForeignKey(Department,on_delete = models.CASCADE)
	courseName = models.CharField(max_length=50,primary_key=True)
	sem = models.IntegerField(default=0,null=True,blank=True)

class Subjects(models.Model):
	deptName = models.ForeignKey(Department,on_delete = models.CASCADE)
	courseName = models.ForeignKey(Courses,on_delete = models.CASCADE)
	sem1 = models.CharField(max_length=100,blank=False,null=False)
	sem2 = models.CharField(max_length=100,blank=False,null=False)
	sem3 = models.CharField(max_length=100,blank=False,null=False)
	sem4 = models.CharField(max_length=100,blank=False,null=False)

class Teacher(models.Model):
	teacherId = models.CharField(max_length=10,primary_key=True)
	teacher_name = models.CharField(max_length=100, blank=False, null=False)

class TeacherResp(models.Model):
	teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,default='0')
	dept = models.CharField(max_length=100)
	course = models.CharField(max_length=100)
	sem = models.IntegerField(default=1)
	subj = models.CharField(max_length=100)
	div = models.CharField(max_length=2)
	isExam = models.IntegerField(default=0,blank=False,null=False)

class studMarks(models.Model):
	examid = models.CharField(max_length=50)
	roll = models.ForeignKey(Student,max_length=10, on_delete = models.CASCADE)
	marks = models.IntegerField(default=0,blank=True,null=True)

class Attendance(models.Model):
	lecId = models.CharField(max_length=50,default='0')
	roll = models.CharField(max_length=10)
	curratt = models.DecimalField(decimal_places=2,max_digits=5,default=0)