from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import PostModel
from .forms import PostForm,UpdatePost
from django.contrib.auth import login,logout ,authenticate
from datetime import datetime
# Create your views here.

def home(request):
	if request.user.is_authenticated:
		data = PostModel.objects.filter(user=request.user)
		return render (request,'home.html',{'data':data})
	else:
		return redirect('ulogin')

def register(request):
	if request.method == "POST":
		fn = request.POST.get('fn')
		ln = request.POST.get('ln')
		em = request.POST.get('em')
		un = request.POST.get('un')
		p1 = request.POST.get('p1')
		p2 = request.POST.get('p2')

		try:
			user = User.objects.get(username=un)
			return render (request,'register.html',{'msg':"Username Already Exist."})
		except User.DoesNotExist:
			try:
				user = User.objects.get(email=em)
				return render (request,'register.html',{'msg':"Email Already Exist."})
			except User.DoesNotExist:
				if p1 == p2:
					user = User.objects.create_user(first_name=fn.capitalize(),last_name=ln.capitalize(),email=em,username=un,password=p1)
					user.save()
					return render(request,'register.html',{'msg':"Register Successfully"})
				else:
					return render(request,'register.html',{'msg':"Password did not match."})

	else:
		return render(request,'register.html')


def ulogin(request):
	if request.method=="POST":
		un = request.POST.get('un')
		pw = request.POST.get('pw')

		usr = authenticate(username=un,password=pw)
		if usr is None:
			return render(request,'ulogin.html',{'msg':"Invalid Credentials."})	
		else:
			login(request,usr)
			return redirect('home')
	else:
		return render(request,'ulogin.html')


def ulogout(request):
	logout(request)
	return redirect("ulogin")


def create(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			text = request.POST.get("text")
			
			p= PostModel(user=request.user,text=text)
			p.save()
			fm = PostForm()
			return render (request,'create.html',{'fm':fm,'msg':"Posted"})			
		else:
			fm = PostForm()
			return render(request,'create.html',{'fm':fm})
	else:
		return redirect("ulogin")



def edit(request,id):
	if request.user.is_authenticated:
		p = PostModel.objects.get(id=id)
		fm = UpdatePost(initial={'id':p.id,'text':p.text})
		fm.fields["id"].widget.attrs["readonly"] = True
		return render (request,"update.html",{"fm":fm})
	else:
		return redirect("ulogin")

def update_post(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			id= request.POST.get("id")
			text = request.POST.get("text")
			try:
				data = PostModel.objects.get(id=id)
				data.text = text
				data.save()
				fm  = UpdatePost()
				return render(request,'update.html',{'fm':fm,"msg":"Post Updated"})
				
			except PostModel.DoesNotExist:
				fm = UpdatePost()
				return render (request,"update.html",{'fm':fm,"msg":"Post Does Not Exist."})
				
		else:		
			fm = UpdatePost()
			return render(request,'update.html',{'fm':fm})
	else:
		return redirect("ulogin")


def delete(request,id):
	if request.user.is_authenticated:
		p = PostModel.objects.get(id=id)
		p.delete()
		return redirect("home")
	else:	
		return redirect("ulogin")


def profile(request):
	if request.user.is_authenticated:
		return render(request,"profile.html")
	else:
		return redirect("ulogin")
	
				
			
