from django.db import models
from django.contrib.auth.models import User

class Brother(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	pledge_class = models.CharField(max_length=20)
	grad_class = models.CharField(max_length=20)
	major = models.CharField(max_length=100, blank=True)
	hometown = models.CharField(max_length=40, blank=True)
	nickname = models.CharField(max_length=40, blank=True)
	family = models.CharField(max_length=20)
	quote = models.CharField(max_length=500, blank=True)
	quote_author = models.CharField(max_length=50, blank=True)
	is_alumni = models.BooleanField(default=False)
	bro_pic = models.ImageField(upload_to="bropics")

	def __unicode__(self):
		return self.first_name + " " + self.last_name

class Rushee(models.Model):
	user = models.OneToOneField(User)
	phone_num = models.CharField(max_length=20)
	dorm = models.CharField(max_length=40)
	grad_class = models.CharField(max_length=20)
	major = models.CharField(max_length=100)
	gpa = models.CharField(max_length=20)
	q1 = models.TextField(blank=True)
	q2 = models.TextField(blank=True)
	q3 = models.TextField(blank=True)
	q4 = models.TextField(blank=True)
	picture = models.ImageField(upload_to="rushpics")
	resume = models.FileField(upload_to="rushresumes")
