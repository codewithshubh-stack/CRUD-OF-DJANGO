from django.shortcuts import render,redirect
from app.models import StudentModel


# Create your views here.


def Student_details(request):
    student=StudentModel.objects.all()
    return render(request,'details.html',{'key': student})

def add_students(request):   
    if request.method == "POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        city=request.POST.get("city")

        StudentModel.objects.create(
            name=name,
            age=age,
            city=city
        )
        return redirect('student_details')


    return render(request,'add.html')

def edit_student(request,id):
    student = StudentModel.objects.get(id=id)

    if request.method=='POST':
        student.name=request.POST.get("name")
        student.age=request.POST.get("age")
        student.city=request.POST.get("city")

        student.save()
        return redirect('student_details')

    return render(request,'edit.html',{'key':student})

