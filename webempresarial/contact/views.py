from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('name', '')
            content = request.POST.get('name', '')
                
            email = EmailMessage(
                "Recibiste un mensaje",
                "De {} <{}> \n\nEscribio: n\n\{}" . format(name, email, content), 
                "no-contestar@inbox.mailtrap.io",
                ["mork.morquecho@gmail.com"],
                reply_to=[email]
            )

            try: 
                email.send
                return redirect(reverse('contact') + "?ok")
            except:
                return redirect(reverse('contact') + "?fail") 

    return render(request, "contact/contact.html", {'form':contact_form})