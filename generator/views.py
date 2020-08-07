from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
	return render(request, 'generator/home.html')


def about(request):
	return render(request, 'generator/about.html')

def password(request):
	length 		= int(request.GET.get('length',5))

	alpha 		= 'abcdefghijklmnopqrestuvwxyz'
	character	= list(alpha.lower())

	if request.GET.get('uppercase'):
		character.extend(list(alpha.upper()))

	if request.GET.get('numbers'):
		character.extend(list('0123456789'))

	if request.GET.get('special'):
		character.extend(list('!@#$&*?'))

	thepassword=''

	for i in range(length):
		thepassword += random.choice(character)

	return render(request,'generator/password.html',{'thepassword':thepassword})