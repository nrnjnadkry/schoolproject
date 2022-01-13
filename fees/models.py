from django.db import models
# from django.db.models.fields import CommaSeparatedIntegerField
from django.core.validators import validate_comma_separated_integer_list
#Database table
#Fee Structure
'''
----------------------------------------
student_name --> text
grade --> integer
department --> text
lastresult --> float
photo --> image
'''
class FeeStructure(models.Model):
    student_name = models.CharField(max_length=150)
    grade = models.IntegerField()
    department = models.CharField(max_length=150)
    lastResult = models.FloatField()
    photo = models.ImageField()
    # fee = models.CommaSeparatedIntegerField(max_length=200)
    fee = models.CharField(validators=[validate_comma_separated_integer_list],max_length=200,default='')
    def __str__(self):
        return self.student_name