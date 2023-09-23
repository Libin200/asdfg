from django.shortcuts import render,redirect
from django.http import HttpResponse
from samapp.models import itdesk,up_load
from samapp.form import itdeskform,uploadform
from samapp.functions import upload
from sampro import settings
from django.core.mail import send_mail
# Create your views here.

def insert(request):
    if request.method=='POST':
        form=itdeskform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                a="please enter valid"
                form=itdeskform()
                return render(request,'aaa.html',{'form':form,'a':a})
        else:
            a="please enter valid"        
            form=itdeskform()
            return render(request,'aaa.html',{'form':form,'a':a})
    else:        
        form=itdeskform()
        return render(request,'aaa.html',{'form':form})

def view(request):
    form=itdesk.objects.all()
    return render(request,'view.html',{'form':form})

def edit(request,id):
    form=itdesk.objects.get(id=id)
    return render(request,'update.html',{'form':form})

def update(request,id):
    form=itdesk.objects.get(id=id)
    form1=itdeskform(request.POST,instance=form)
    if form1.is_valid():
        form1.save()
        return redirect('/view')
    else:
        return render(request,'update.html',{'form':form})

def destroy(request,id):
    a=itdesk.objects.get(id=id)
    a.delete()
    return redirect('/view')

def upload1(request):
    if request.method=="POST":
        form=uploadform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            upload(request.FILES['file'])
            return HttpResponse("upload successfully")
        else:
            return HttpResponse("the file is does not upload")
    else:
        form=uploadform()
        return render(request,"upload.html",{'form':form})
    
def mail1(request):
    to='samuelmathoor11@gmail.com'
    subject='do or die'
    body='just fun'
    a=send_mail(subject,body,settings.EMAIL_HOST_USER,[to])
    if a==1:
        return HttpResponse('mail sent successfully')
    else:
        return HttpResponse('mail was not sent successfully')
