from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):

    title = models.CharField(max_length = 30)
    content =models.TextField()
    author = models.ForeignKey(User, related_name= 'course',on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'course-pics')
    duration = models.PositiveIntegerField()
    is_new = models.BooleanField( default = False)
    price = models.PositiveIntegerField()
    creation_date = models.DateTimeField(default = timezone.now)
    Updating_date = models.DateTimeField(auto_now = True)

    def __str__(self):

        return self.title

