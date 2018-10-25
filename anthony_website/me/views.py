from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from smtplib import SMTPSenderRefused
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

# Create your views here.

class contactView(TemplateView):
    template_name = "me/contact_form.html"

    def get(self, request):
        form = ContactForm()
        homepage= 'Anthony Sukadil'
        contact_context = {
            # 'email_context':form.email_address,
            # 'message_context':form.message,
            "form_context":form,
            "title": homepage
        }
        return(render(request, self.template_name, contact_context))

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['message']
            email_message_obj = EmailMessage(
                subject=email + " " + subject,
                body=text,
                from_email=email,
                to=['anthonysukadil1@gmail.com']
            )
            message= "Message sent!"
            contact_context ={
                'email':email,
                'text':text,
                'form_context':form,
                'message': message,
            }
            try:
                # send_mail(subject,message,email, ["anthonysukadil1@gmail.com"])
                email_message_obj.send()
                # print("hi")
            except BadHeaderError:
                return(render(request, 'me/404.html'))
            except SMTPSenderRefused:
                return(render(request, 'me/404.html'))
            return(render(request, self.template_name, contact_context))
        else:
            message= "Message failed to send, try refreshing the page again."
            contact_context ={
                'message': message,
            }
            return(render(request, self.template_name, contact_context))

def error_400(request):
    return(render(request, 'me/404.html'))

def error_403(request):
    return(render(request, 'me/404.html'))

def error_404(request):
    return(render(request, 'me/404.html'))

def error_500(request):
    return(render(request, 'me/404.html'))