from django.shortcuts import render,redirect
from my_app.models import student
from my_app.form import StudentForm
# Create your views here.
def first_page(request):
    return render(request,"firstpage.html")
def about_us(request):
    return render(request,"ABOUT.html")
def overview(request):
    return render(request,"OVERVIEW.html")
def vission(request):
    return render(request,"VISSION.html")
def admission(request):
    return render(request,"ADMISSION.html")
def showstudent(request):
    students=student.objects.all()
    return render(request,"students.html",{'students':students})
def save(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/showstudent/")