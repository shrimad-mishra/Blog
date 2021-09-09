from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from froala_editor.fields import FroalaField

class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    
class BlogModel(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    content = FroalaField()
    user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='public')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)
