from django.db import models

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=40)
    esal=models.FloatField()
    passw=models.CharField(max_length=40)
    rpass=models.CharField(max_length=40)
    def __str__(self):
        return self.ename
