from django.shortcuts import render,HttpResponseRedirect

from .models import User
from .forms import StudentRegistration
# Create your views here.
# Add new data and show them in this function

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=ps)
            reg.save()
        fm = StudentRegistration()
            
    else:
       fm = StudentRegistration()
    std=User.objects.all()
    return render(request,'roll/a&s.html',{'form':fm,'stu':std})



# to update/edit the data from this function

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'roll/update_student.html',{'form':fm})

# Delete the data from this function
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')