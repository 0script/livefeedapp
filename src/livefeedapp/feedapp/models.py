from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    tel=models.CharField(max_length=30)
    pass


class Post(models.Model):
    'Model For making post'
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=22)
    text=models.CharField(max_length=280)
    date_posted=models.DateTimeField(auto_now_add=True)
    hidden=models.BooleanField(default=False)
    date_hiden=models.DateTimeField(blank=True,null=True)
    hidden_by=models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='Janny Who Hide+')

    def __str__(self):
        return self.text

class Report(models.Model):
    reported_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     return reverse("Post_detail", kwargs={"pk": self.pk})

