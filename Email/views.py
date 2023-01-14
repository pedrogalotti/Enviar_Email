from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives # enviar email
from django.template.loader import render_to_string # fazer conversão para email-
from django.utils.html import strip_tags # remove tudo oque se paresse com uma tag html da nossa string
from django.conf import settings

def enviar_email(request):

    html_content = render_to_string('emails/cadastro_confirmado.html', {'nome': 'Pedro Lucas'}) # informar o caminho do templates (você pode enviar dados se quiser)
    text_content = strip_tags(html_content) # retirar tudo oque se paressa tag html
    #   wwalter.carlos7@gmail.com
    email = EmailMultiAlternatives('Cadastro confirmado', text_content, settings.EMAIL_HOST_USER, ['coloque o email para quem será enviado']) # assunto, corpo do email (no caso é o 'text_content' feito a cima)
    email.attach_alternative(html_content, 'text/html')
    email.send()

    return HttpResponse('Email enviado')