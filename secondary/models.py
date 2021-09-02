from django.db import models
from django.db.models.aggregates import Max
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.



class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    message = models.TextField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Parent(models.Model):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    first_name = models.CharField(max_length=200, null=True)
    middle_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, choices=SEX, default='Male')
    country = CountryField(default='NG')
    state = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # one to one field with User
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Staff(models.Model):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    first_name = models.CharField(max_length=200, null=True)
    middle_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, choices=SEX)
    address = models.CharField(max_length=200, null=True)
    country = CountryField(default='NG')
    state = models.CharField(max_length=200, null=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    # one to one field with User
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# subjects

class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True, blank=False)
    teacher = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.subject_name

class Student(models.Model):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    CLASS = (
        ('JSS1', 'JSS1'),
        ('JSS2', 'JSS2'),
        ('JSS3', 'JSS3'),
        ('SS1', 'SS1'),
        ('SS2', 'SS2'),
        ('SS3', 'SS3'),
    )
    first_name = models.CharField(max_length=200, null=True)
    middle_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, choices=SEX, null=True)
    level = models.CharField(max_length=200, choices=CLASS, null=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True, blank=False)
    country = CountryField(default='NG')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # one to one field with User
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    # student's parent
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True)

    # subjects
    subjects = models.ManyToManyField(Subject)


    def __str__(self):
        return self.first_name + ' ' + self.last_name






