from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Records
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse


def user_signup(request):
    if request.method=='GET':
        form=UserCreationForm()
        return render(request,"signup.html",{"form":form})
    else:
        user=UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
        return redirect('/login/')        


def user_login(request):
    form=request.POST
    if request.method == 'POST':
        username = form['username']
        password = form['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            print("logged in")
            return redirect('/front/')
        else:
            return redirect('/login/')
    return render(request,"login.html")        


@login_required(login_url="/login/")
def front(request):
    return render(request,"front.html")

@login_required(login_url="/login/")
def showbook(request):
    data=list(models.Library.objects.all().values())
    return render(request,"showbook.html",{"data":data})


@login_required(login_url="/login/")
def addbook(request):
    return render(request,"addbooks.html")


@login_required(login_url="/login/")
def inputbook(request):
    data=dict(request.GET)

    id=int(data['id'][0])
    name = data['name'][0]
    subject = data['subject'][0]
    description = data['description'][0]
    semester = int(data['semester'][0])
    quantity = int(data['quantity'][0])
    price = int(data['price'][0])
    books=models.Library(id=id,name=name,subject=subject,description=description,semester=semester,quantity=quantity,price=price)
    books.save()
    data=list(models.Library.objects.all().values())
    return render(request,"showbook.html",{"data":data})

@login_required(login_url="/login/")
def delete(request,id):
    # pro=dict(request.GET)
    pro=models.Library.objects.get(id=id)
    pro.delete()
    data=models.Library.objects.all()
    return render(request,"showbook.html",{"data":data})

@login_required(login_url="/login/")
def editbook(request,id):
    data=models.Library.objects.get(id=id)
    if request.method == 'POST':
        data.id=request.POST.get('id')
        data.name=request.POST.get('name')
        data.subject=request.POST.get('subject')
        data.description=request.POST.get('description')
        data.semester=request.POST.get('semester')
        data.quantity=request.POST.get('quantity')
        data.price=request.POST.get('price')
        data.save()
        return redirect('/showbook/')
    return render(request,"edit.html",{"data":data})


@login_required(login_url="/login/")
def showissue(request):
    data=list(models.Records.objects.all().values())
    # book=list(models.Library.objects.all().values())
    # member=list(models.datamember.objects.all().values())
    return render(request,"showissue.html",{"data":data})

@login_required(login_url="/login/")
def issue(request):
    return render(request,"issue.html")

@login_required(login_url="/login/")
def inputissue(request):
    data=dict(request.GET)
    print(data)
    member=data['member_id'][0]
    book=data['book_id'][0]
    d=models.datamember.objects.get(id=member)
    b=models.Library.objects.get(id=book)
    print(d)
    print(b.name)
    # id=(data['id'][0])
    # member_id = data['member_id'][0]
    # book_id = data['book_id'][0]
    issue_date = (data['issue_date'][0])
    return_date = (data['return_date'][0])
    status = data['status'][0]
    issue_date = timezone.now().date()
    return_date = issue_date + timedelta(days=5)
    max_return_date = return_date
    page=models.Records(member_id=d,book_id=b,issue_date=issue_date,return_date=return_date,status=status)
    b.quantity-=1
    b.save()
    page.save()
    data=list(models.Records.objects.all().values())
    return redirect('/showissue/')
    return render(request,"showissue.html",{"data":data})


@login_required(login_url="/login/")
def issuebook(request):
    print("-------------one--------------------------------")
    data=request.GET.get('book_id')
    print("-------------two--------------------------------")
    # if request.method =='post':
    #     data=request.post.get('book_id')
    #     # data.book_name=request.post.get('book_name')
    #     print(data)
    #     return redirect("/showissue/")
    return render(request,"issue.html",{"data":data})

# @login_required(login_url="/login/")
# def filterstudent(request,id):
#     data=models.Records.objects.get(id=id)
#     data.delete()
#     data=models.Records.objects.all()
#     return render(request,"showissue.html",{"data":data})
       
@login_required(login_url="/login/")
def update(request,id):
    data=models.Records.objects.get(id=id)
    if request.method == 'POST':
        data.status = request.POST.get('status')
        if data.status == 'return':
            b=models.Library.objects.get(id=id)
            b.quantity+=1
            b.save()
        elif data.status == 'issue':
            b=models.Library.objects.get(id=id)
            b.quantity-=1
            b.save()    
        data.save()
        return redirect('/showissue/')
    return render(request,"update.html",{"data":data})



def user_logout(request):
    logout(request)
    print("logged out")
    return redirect('/login')



@login_required(login_url="/login/")
def showstd(request):
    data=list(models.datamember.objects.all().values())
    return render(request,"showstd.html",{"data":data})

@login_required(login_url="/login/")
def addstudent(request):
    return render(request,"addstudent.html")

@login_required(login_url="/login/") 
def inputstudent(request):
    data=dict(request.GET)
    ID=int(data['id'][0])
    name=data['name'][0]
    mobile=int(data['mobile'][0])
    semester=int(data['semester'][0])
    branch=data['branch'][0]
    data_meme=models.datamember(ID,name=name,mobile=mobile,semester=semester,branch=branch)
    data_meme.save()
    data=list(models.datamember.objects.all().values())
    return render(request,"showstd.html",{'data':data})

@login_required(login_url="/login/")
def Mdelete(request,id):
    pro=models.datamember.objects.get(id=id)
    pro.delete()
    data=models.datamember.objects.all()
    return render(request,"showstd.html",{"data":data})

@login_required(login_url="/login/")
def Medit(request,id):
    data=models.datamember.objects.get(id=id)
    if request.method == 'POST':
        data.id=request.POST.get('id')
        data.name=request.POST.get('name')
        data.mobile=request.POST.get('mobile')
        data.semester=request.POST.get('semester')
        data.branch=request.POST.get('branch')
        data.save()
        return redirect('/showstd/')
    return render(request,"Memberedit.html",{"data":data})

@login_required(login_url="/login/")
def about(request):
    return render(request,"about.html")  


