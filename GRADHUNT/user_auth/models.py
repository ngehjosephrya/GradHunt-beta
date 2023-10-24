from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    is_online = models.BooleanField(default=False)
    following = models.ManyToManyField(User, related_name="following", blank=True)
    friends = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='friend_of')
    friendship_requests = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='requested_by')
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    
