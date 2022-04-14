from enum import unique
from django.db import models
from account.models import CustomUser as User
# Create your models here.
class addClass(models.Model):
    classname = models.CharField(max_length = 30, null=True, unique=True, default='')
    profname = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.classname