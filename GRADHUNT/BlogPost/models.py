from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField( default='default.png', upload_to='post_pics', 
                              validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    class Meta:
        ordering = ['-date_posted','-author']
    
    def __str__(self):
        return self.title

