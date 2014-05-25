from django.db import models

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