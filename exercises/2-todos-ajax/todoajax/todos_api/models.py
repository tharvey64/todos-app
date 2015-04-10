from django.db import models
from datetime import datetime
import hashlib
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=50)
    key = models.CharField(max_length=100,unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.key:
            datetime_str = str(datetime.now())
            self.key = hashlib.md5((self.username + datetime_str).encode('utf-8')).hexdigest()
        super().save(*args, **kwargs)

class Todo(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)