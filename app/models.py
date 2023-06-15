from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    edept=models.CharField(max_length=100)
    ename=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)

    def __str__(self):
        return self.ename