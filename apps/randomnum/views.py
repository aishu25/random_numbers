from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def random(request):
	if "counter" not in request.session:
		request.session["counter"] = 1
	else:
		request.session["counter"] += 1 
	context = {
		"unique_id" : get_random_string(length=12)
	}
	return render(request,'randomnum/index.html',context)