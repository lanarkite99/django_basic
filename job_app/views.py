from django.shortcuts import render
from .forms import AppForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method=="POST":
        form=AppForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            email=form.cleaned_data["email"]
            date=form.cleaned_data["date"]
            occupation=form.cleaned_data["occupation"]
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email,date=date,occupation=occupation)
            message_body=f"{first_name},you have submitted the application. Thanks you"
            email_message=EmailMessage("Confirmation for job app submission",
                                       message_body,to=[email])
            email_message.send()

            messages.success(request,"Details submitted successfully")
    return render(request,"index.html")

def about(request):

    return render(request,"about.html")
