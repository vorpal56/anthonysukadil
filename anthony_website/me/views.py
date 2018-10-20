from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.static import serve
from pathlib import os
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request,"me/contact_form.html")


class contactView(TemplateView):
    template_name = "me/contact_form.html"

    def get(self, request):
        form = ContactForm()
        contact_context = {
            # 'email_context':form.email_address,
            # 'message_context':form.message,
            "form_context":form,
            "form_ul":form.as_ul,
            "form":form.as_p
        }
        return(render(request, self.template_name, contact_context))

    def post(self, request):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            print(email)
            text = form.cleaned_data['message']
            contact_context ={
                'email':email,
                'text':text
            }
            return(render(request, self.template_name, contact_context))
        # return(render(request, self.template_name))