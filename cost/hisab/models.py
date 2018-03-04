from django.db import models

# Create your models here.

class Hisab(models.Model):
	taka = models.IntegerField()
	purpose = models.CharField(max_length=250)
	date = models.DateTimeField(auto_now_add=True)

	def __str(self):
		return self.purpose
