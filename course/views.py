from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.http import HttpResponse

from course.models import Department, Student

def index(request):
    department = Department.objects.all()  #>> Select * from department;
    department = Department.objects.get(id=1) #>> Select * from department where id=1;
    departments = Department.objects.filter(no_of_teachers=10) # Select * from department where no_of_teachers=10;
    departments = Department.objects.filter(id=1)

    current_time = datetime.now()

    html = f'<html>\
            <body>\
                    <table>\
                    <tr>\
                        <th>ID</th>\
                        <th>Department<th>\
                    </tr>\
                    <tr>\
                        <td>{department.id}</td>\
                        <td>{department.name}</td>\
                    </tr>\
                    </table>\
            </body>\
            </html>'

    try:
        department = Department.objects.get(id=5)
        print(department)
    except Exception as e:
        print (str(e))

    # return HttpResponse(f'ID : {department.id},Name :{department.name},No of Teachers :{department.no_of_teachers}')
    return HttpResponse(html)


def learn_django(request):
    return HttpResponse('<h1>Hello Django</h1>')


def learn_document(request):

    departments = Department.objects.all()

    context = {
        'departments':departments,
        'table_name':'Departments'
    }

    return render(request,'courseone.html',context)

def show_student(request):

    students= Student.objects.all()
    
    context = {
        'students':students,
        'table_name':'Students'
    }

    return render(request,'coursetwo.html',context)