import students
from django.shortcuts import get_object_or_404, render, redirect
from students.forms import StudentsForm
from students.models import Student

# Create your views here.

def std(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        form.save()
        return redirect('/view')
    else:
        form=StudentsForm()
    return render(request,'index.html',{'form':form})

def view(request):
    students = Student.objects.all()
    return render(request,"view.html",{'students':students})

def delete(request, id):
    students = Student.objects.get(id=id)
    students.delete()
    return redirect("/view")

def edit(request, id):
    students = Student.objects.get(id=id)
    return render(request,'edit.html',{'students':students})

def update(request, id):

        students = Student.objects.get(id=id)

        if request.method == 'GET':
                form = StudentsForm(instance=students)
                return redirect("/view")

        else:
                form = StudentsForm(request.POST, instance=students)
                form.save()
                return redirect("/view")

def add(request):
    return redirect("/std")
