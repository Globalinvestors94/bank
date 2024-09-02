from django.db import models


class ScreenRecording(models.Model):
	video_file = models.FileField(upload_to='recordings/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Recording {self.id} uploaded at {self.uploaded_at}"

# Create your models here.
