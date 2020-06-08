from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    protfolio=models.URLField(blank=True)
    profilePic=models.ImageField(upload_to='profile_pics',blank=True)


    def __str__(self):
        return self.user.username

