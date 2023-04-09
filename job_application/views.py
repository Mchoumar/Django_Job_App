from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    # Checks if the method is posted and gets the data posted
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            # Stores the data inside the database table
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            messages.success(request, "Form was submitted successfully!")

            message_body = f"A new job application was submitted. Thank you, {first_name}."
            # Email setup using django
            email_message = EmailMessage("Form submission confirmation", message_body, to=[email])
            email_message.send()

    # Renders the html file
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
