from django.db import models
from django.contrib.auth.models import User
from django.db.models import FileField

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

class ContentTypeRestrictedFileField(FileField):
	def __init__(self, *args, **kwargs):
	    self.content_types = kwargs.pop("content_types")
	    self.max_upload_size = kwargs.pop("max_upload_size")

	    super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

	def clean(self, *args, **kwargs):        
	    data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)

	    file = data.file
	    try:
	        content_type = file.content_type
	        if content_type in self.content_types:
	            if file._size > self.max_upload_size:
	                raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
	        else:
	            raise forms.ValidationError(_('Filetype not supported.'))
	    except AttributeError:
	        pass        

	    return data

class Rushee(models.Model):
	user = models.OneToOneField(User)
	phone_num = models.CharField(max_length=20)
	dorm = models.CharField(max_length=40)
	grad_class = models.CharField(max_length=20)
	major = models.CharField(max_length=100)
	gpa = models.CharField(max_length=20)
	picture = models.ImageField(upload_to="rushpics")
	resume = ContentTypeRestrictedFileField(upload_to="rushresumes", 
		  								    content_types=['application/pdf'],
											max_upload_size=26214400,
											blank=True,
											null=True)

class Question(models.Model):
	content = models.TextField()

class Answer(models.Model):
	text = models.TextField()
	question = models.ForeignKey(Question)
	rushee = models.ForeignKey(Rushee)
