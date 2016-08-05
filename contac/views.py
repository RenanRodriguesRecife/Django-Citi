from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.generic import View, TemplateView

from .forms import ContactForm

class IndexView(TemplateView):
	template_name = 'index.html'

def contact(request):
	if request.method =='POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			messages = form.cleaned_data['messages']
			subject = '[DjangoEcommerce] %s entrou em contato' % name
			body = 'E-mail: %s\n%s' % (email, message)
			send_mail(subject,body,'admin@example.com',['contato@admin.com'])
			form = ContactForm()

		else:
			messages.error(request,'Formulário inválido')
	else:
		form = ContactForm()
	context = {

		'form':form
	}
	return render(request,'contact.html',context)