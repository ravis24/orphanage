from django.shortcuts import render, redirect

# Create your views here.
from django.http import *
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q

def signup(request):
	if request.method == 'POST':
		form=signup_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/blood/signup/')
	else:
		form = signup_form()
	return render(request, 'signup.html', {'form':form})

def contact(request):
	if request.method == 'POST':
		form=contact_form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/blood/contact/')
	else:
		form = contact_form()
	return render(request, 'contact.html', {'form':form})
def  feedback(request):
	if request.method == 'POST':
		form=share_feedback(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/blood/index/')
	else:
		form = share_feedback()
	return render(request, 'feedback.html', {'form':form})
def tips(request):
	if request.method == 'POST':
		form=find_donor(request.POST)
		return HttpResponseRedirect('blood/signup/')
	else:
		form = find_donor()
	return render(request, 'tips.html', {'form':form})

def find(request):
	if request.method == 'POST':
		form=find_donor(request.POST)
		return HttpResponseRedirect('/blood/find/')
	else:
		form=find_donor()
		query=Register12.objects.all()
	return render(request,"find.html",{'query':query,'form':form})

def donor_feedback(request):
	if request.method == 'POST':
		form=find_donor(request.POST)
		return HttpResponseRedirect('blood/signup/')
	else:
		form = find_donor()
		query=donar_feedback.objects.all()
	return render(request, 'donor_feedback.html', {'query':query,'form':form})

def donate(request):
	if request.method == 'POST':
		srch=request.POST['blood_group']
		if srch:
			match=Register12.objects.filter(Q(blood_group__icontains=srch))
			if match:
				return render(request,'find.html',{'sr':match})
			else:
				messages.error(request,'no result found')
		else:
			return HttpResponseRedirect('/blood/find/')
	return render(request,'donate.html')

def apply_v(request):
	if request.method == 'POST':
		form=volunterr_form(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/blood/success/')
	else:
		form = volunterr_form()
	return render(request, 'apply_volunteer.html', {'form':form})
def success(request):
	return HttpResponse('successfuly uploaded')

def childpro(request):
    return render(request,'child_protection.html')

def nonprofit(request):
    return render(request,'startnonprofit.html')
def supporter(request):
    return render(request,'supporters.html')
def life(request):
    return render(request,'life_as_a_volunteer.html')
def goods(request):
    return render(request,'donategoods.html')
def sponsor(request):
    return render(request,'sponsor.html')
def mstatement(request):
    return render(request,'missionstatement.html')
def home(request):
    return render(request,'home.html')


