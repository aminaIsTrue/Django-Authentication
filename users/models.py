from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.






class Profile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'pictures', default = '1.jpg')

    def __str__(self):
        
        return "{} profile".format(self.user.username) # for python 3.6 +

def create_profile(sender,**kwargs):
    #print(kwargs.instance)
    if kwargs.get('created') :
        user = kwargs.get('instance')
        Profile.objects.create(user = user)

post_save.connect(create_profile, sender = User)




