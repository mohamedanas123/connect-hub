from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    des=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title +'\n' +self.des