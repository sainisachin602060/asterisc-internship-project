from django.shortcuts import render,redirect



from .models import User,Blog,QuerySend

from django.http import HttpResponse

from django.contrib import messages

from django.contrib.sessions.models import Session




#Home Page View
def Home(request):
    return render(request,'Home.html')



#login page to redirect admin to autheticate pages
def login(request):
    return render(request,'login.html')


#user query handle to this methods
def sendQuery(request):
 
        if request.method=='POST':
            uname=request.POST['uname']
            uemail=request.POST['uemail']
            queryms=request.POST['query']
            Qobject=QuerySend(uname=uname,uemail=uemail,query=queryms)
            Qobject.save()
            return redirect('sendQuery')

        else:
            return render(request,'query.html')  
  

#login admin into database
def loged(request):
    if request.method=='POST':
        uemail=request.POST['uemail']
        upassword=request.POST['upassword']
        
        
        if User.objects.filter(uemail=uemail).exists():
            output=User.objects.filter(uemail=uemail,upassword=upassword).count()
            if output>0:
                return redirect('/admin/')
            else:
               messages.error(request,"wrong email address and password")
               return redirect('login')    
                
        else:
            
            messages.error(request,"you are not registerd please contact to admin ")
            return redirect('login')       
                
    else:
        return redirect('login')
    
    
#load all blog data   
def blog(request):
    data=Blog.objects.all()
    return render(request,'blog.html',{'data':data}) 
            

#read a particuler post
def readPost(request,id):
    blogdata=Blog.objects.get(id=id) 
    blogdata.view+=1
    blogdata.save()
    
   
    return render(request,'eachpost.html',{'blogdata':blogdata})

#brief introduction to our blog application
def About(request):
    return render(request,'About.html')


#search a particuler blog using his technology
def Searching(request):
    if request.POST:
        cat=request.POST['category']
        CatData=Blog.objects.filter(Catogery__icontains=cat)
        if CatData:
            return render(request,'blog.html',{'CatData':CatData})
        else:
            message=messages.error(request,"No Blog Found realted to this Category ")
            return render(request,'blog.html')
        
    else:
        return redirect('/blog/')    
     
        
        
    
    







