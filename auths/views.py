from django.shortcuts import render,redirect
from .forms import FormularioRegistro
from .models import UserAuth
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.http import HttpResponse

from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime 
# Create your views here.

def login_view(request):
    if request.method == "POST":
        
        email = request.POST["email"] 
        password = request.POST["password"] 
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("home:home")
        else:
            messages.error(request,"Datos inválidos")
            return redirect("auths:login")  
    return render(request,"auths/login.html")
    
def logout_view(request):
    auth.logout(request) 
    messages.success(request, "Has cerrado sesión satisfactoriamente")
    return render(request,"auths/login.html")

def signin_view(request):
    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        
        if formulario.is_valid():            
            nombre = formulario.cleaned_data["nombre"]
            apellido = formulario.cleaned_data["apellido"]
            email = formulario.cleaned_data["email"]
            password = formulario.cleaned_data["password"]
            telefono = formulario.cleaned_data["telefono"] 
            
            username = email.split("@")[0] 
            
            user = UserAuth.objects.create_user(
                nombre=nombre, 
                apellido=apellido, 
                email=email, 
                password=password, 
                username=username, 
            )
            
            user.telefono = telefono
            user.save()
            
            current_site = get_current_site(request)
            subject = "Hola, debes activar tu cuenta para acceder"
            html_body = "auths/verify_account.html"
            
            body_mail =  render_to_string(html_body,{
                "user" : user,
                "domain" : current_site,
                "uid" : urlsafe_base64_encode(force_bytes(user.pk)),
                "token" : default_token_generator.make_token(user),
                "current_year" : datetime.now().year,
            })
            
            to_email = email
            
            send_email = EmailMultiAlternatives(subject,body_mail,to=[to_email],)
            send_email.attach_alternative(body_mail,"text/html")
            send_email.send()
            
            messages.success(request, "Se ha registrado correctamente. Revise su correo")
            
            return redirect("auths:signin")
            
            
    else:
        formulario = FormularioRegistro()
        
    
    context = {
        "formulario": formulario,
    } 
    
    return render(request, "auths/register.html" ,context=context)

def verify_account(request, uidb64, token):
    uid = urlsafe_base64_decode(uidb64).decode()
    user = UserAuth._default_manager.get(pk=uid)
    
    #aun le falta a esto, no?
    
    return HttpResponse(f"<h1>OK</h1>")

