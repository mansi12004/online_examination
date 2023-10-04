from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Test(models.Model):
    question = models.CharField(max_length = 200)
    answer = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    total_score = models.IntegerField() 