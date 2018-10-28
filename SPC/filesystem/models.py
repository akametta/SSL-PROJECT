from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class file_model(models.Model):
	file = models.FileField(upload_to='users_files')
	date_posted = models.DateTimeField(default = timezone.now)
	owner = models.ForeignKey(User,on_delete= models.CASCADE)
	def __str__(self):
		return f'{self.file}'
