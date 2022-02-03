from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.core.mail import send_mail


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        sender = request.POST.get("sender")
        email = request.POST.get("email")
        mymessage = request.POST.get("message")

        subject = f'Message From {sender}'
        message = f'{mymessage}'
        n = settings.EMAIL_HOST_USER
        email_from = email
        recipient_list = [n, ]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'home.html')
