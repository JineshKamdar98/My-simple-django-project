from django.db import models

class Channel(models.Model):
	writer=models.CharField(max_length=250)
	channel_title=models.CharField(max_length=500)
	genre=models.CharField(max_length=100)
	channel_logo=models.CharField(max_length=1000)

	def __str__(self):
		return self.channel_title + ' - ' + self.writer

class Series(models.Model):
	chennel=models.ForeignKey(Channel, on_delete=models.CASCADE)
	file_type=models.CharField(max_length=10)
	title=models.CharField(max_length=250)

	def __str__(self):
		return self.title
		
