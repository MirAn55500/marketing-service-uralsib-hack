from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.login


