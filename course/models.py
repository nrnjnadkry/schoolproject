from django.db import models
from django.db.models.enums import Choices


# Database tables
# Student
'''
Fields
-------------------------
name --> text
roll_no --> integer
section --> text (A,B,C,D)
gender--> text (Male, Female, Others)
class  --> integer
department --> Text
phone_no  --> text
email  -- text (email)
address  -- text
is_present -- boolean
bio --> large text
'''

class Department(models.Model):
    name = models.CharField(max_length=150)
    no_of_teachers = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Student(models.Model):

    # Gender Choices  -- > Male, Female, Others
    GENDER_CHOICES = [('M','Male'),
                        ('F','Female'),
                        ('O','Others')
                    ]

    name = models.CharField(max_length=100) #  Text field --> CharField
    roll_no = models.IntegerField(unique=True)
    section = models.TextChoices('A','B')
    gender = models.CharField(max_length=10,blank=True,null=True,choices=GENDER_CHOICES)
    grade = models.IntegerField(verbose_name='Class')
    phone_no = models.CharField(max_length=10)
    dob = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=150,blank=True,null=True)
    is_present = models.BooleanField(default=False)
    bio = models.TextField(blank=True,null=True)
    department = models.ForeignKey(Department ,blank=True,null=True, on_delete=models.SET_NULL)
    website = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name

class GirlStudent(Student):
    last_mensuration_date= models.DateField()



# 1 Student =1 Department
# 1 Department = multiple student (FK = student)