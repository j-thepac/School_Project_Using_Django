from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):return render(request,template_name="home.html")

def addStudent(request):
    if(request.method=="GET"): return render(request,template_name="add.html")
    elif(request.method=="POST"):
        name=request.POST["name"]
        age=int(request.POST["age"])
        classStudent=getClass(age)
        student=Student(getMaxID()+1,name,age,classStudent)
        student.save()
        return render(request,template_name="add.html",context={"data":"Added "})


def getMaxID()->int: return  len(Student.objects.all())
def getClass(age:int)->int:
	if (age < 5 ): return 'kindergarden'
	elif (age > 5  and age < 15): return  (f"class {age-5}")


def getAllStudents(request):
    students=Student.objects.all()
    return render(request,template_name="all.html",context={"students":students})
