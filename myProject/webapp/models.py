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
	roll = models.IntegerField()
	name = models.CharField(max_length=100,blank=False,null=False)
	phone  = models.CharField('Phone number', max_length=10, validators=[MinLengthValidator(10)])
	emailP = models.EmailField(max_length=100)
	address = models.CharField(max_length=1000)
	dept = models.CharField(max_length=50)
	course = models.CharField(max_length=50)
	doj = models.DateField()
	puname = models.ForeignKey(Parent,on_delete = models.CASCADE, default='0')

