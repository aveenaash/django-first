from django.shortcuts import render
from django.http import HttpResponse

from .models import Customer

def index(request):
	customers = Customer.objects.all()[:10]
	context = {
		"customers" : customers
	}
	return render(request,"index.html", context)

def details(request, customer_id):
	customer = Customer.objects.get(id=customer_id)
	var = {
		"customer" : customer
	}
	return render(request,"details.html", var)
