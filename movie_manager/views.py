from django.shortcuts import render,redirect
from movie_manager.models import Entry
from movie_manager.form import MovieForm
from django.contrib import messages
# Create your views here.
def index(request):
	
	return render(request,'index.html')

def list(request):
	all_entries = Entry.objects.all()
	return render(request,'list.html',{'all_entries':all_entries})

def entry(request):
	if request.method=='POST':
		form=MovieForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,('New movie entered!!'))
			return redirect('entry')
	else:
		form=MovieForm()
	return render(request,'entry.html',{'form':form})