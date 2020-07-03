from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import Callback
from .forms import CallbackForm


def record_callback(request):
    form = CallbackForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        phone = form.cleaned_data.get('phone')
        whenToCall = form.cleaned_data.get('whenToCall')
        email = form.cleaned_data.get('email')
        callback = Callback(
            name=name,
            phone=phone,
            whenToCall=whenToCall,
            email=email
        )

        message = f'Имя: {name}\nТелефон: {phone}\nКогда позвонить: {whenToCall}\nПочта: {email}'
        send_mail(
            "Запрос на обратную связь",
            message,
            '"maximokna.ru" <settings.EMAIL_HOST_USER>',
            [['maksim.naumov1889@gmail.com']]
        )
        callback.save()

    return HttpResponseRedirect("")


def callback_page(request):
    return render(request, "callback/callback-page.html")
