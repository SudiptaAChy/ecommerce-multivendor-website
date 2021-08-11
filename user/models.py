from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model) :
    user = models.ForeignKey(User, related_name='user_info', on_delete=models.CASCADE)
    fname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)
