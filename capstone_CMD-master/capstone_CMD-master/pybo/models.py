from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import timezone
import datetime

class business_apply(models.Model):

    name = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    assign_num = models.CharField(max_length=4)
    Living = models.CharField(max_length=100)
    gender = models.CharField(max_length=5)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    office = models.CharField(max_length=10)
    create_date = models.DateTimeField()

def __str__(self):
    return self.name



class Question(models.Model):
    Car_num = models.CharField(max_length=15)
    Car_variety = models.CharField(max_length=10)
    Car_manager = models.CharField(max_length=10)
    bussiness_num = models.CharField(max_length=4)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)


def __str__(self):
    return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class CMD_Question(models.Model):
    pdf = models.FileField(upload_to='books/pdfs/')
    subject = models.CharField(max_length=200)
    Car_num = models.CharField(max_length=15)
    bussiness_manager = models.CharField(max_length=10)
    bussiness_num = models.CharField(max_length=4)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    start_date = models.DateTimeField()
    start_pos = models.CharField(max_length=10)
    destination_pos = models.CharField(max_length=10)

    depart_date = models.CharField(max_length=25)
    arrive_date = models.CharField(max_length=25)

    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    Lat = models.CharField(max_length=30)
    Long = models.CharField(max_length=30)


class CMD_Answer(models.Model):
    cmd_question = models.ForeignKey(CMD_Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
