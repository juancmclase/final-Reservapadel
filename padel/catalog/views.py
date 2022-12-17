




from django.shortcuts import redirect, render,HttpResponse
from django.views import generic
from django.views.generic.list import ListView
from .models import Club, Pistas,Reservas,Contacto,Hora
from .forms import ContactoForm,CustomUserCreationForm,PistasForm,DisponibleForm,UserProfile,HoraForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import FormView,UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
  
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_visits':num_visits},
    )

def quien1(request):

    return render(
        request,
        'quien.html', 
    )

def contacto(request):
    data ={
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario =ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Formulario enviado con exito!"
            #asunto = 'Una persona quiere contactar con nosotros'
            #mensaje1 ="Nombre: "+formulario.cleaned_data['nombre']+" Correo: "+ formulario.cleaned_data['correo']+" Mensaje: "+ formulario.cleaned_data['mensaje']
            #email_from = settings.EMAIL_HOST_USER
            #recipent_list=["juanjocmclase@gmail.com"]
            #send_mail(asunto,mensaje1,email_from,recipent_list)
        else:
            data["form"] = formulario
    return render(request,'contacto.html',data)

def hora(request):
    data ={
        'form': HoraForm()
    }
    if request.method == 'POST':
        formulario =HoraForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Formulario enviado con exito!"
        else:
            data["form"] = formulario
    return render(request,'hora.html',data)

def registro(request):
    data={
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario =CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request, "Te has registrado Correctamente")
            return redirect(to="index")
            
        data["form"] = formulario
    return render(request,'registro.html', data)


def apistas(request):
    data ={
        'form': PistasForm()
    }
    if request.method == 'POST':
        formulario = PistasForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="Formulario enviado con exito!"
        
        data["form"] = formulario
    return render(request,'pistas.html',data)




def mirar_disponibilidad(pista,fecha,hora):
    dis_list = []
    reserva_list= Reservas.objects.filter(pista=pista)
    for reserva in reserva_list:
        if reserva.fecha != fecha and reserva.hora != hora:
            dis_list.append(True)
        elif reserva.fecha != fecha and reserva.hora == hora:
             dis_list.append(True)
        elif reserva.fecha == fecha and reserva.hora != hora:
             dis_list.append(True)
        else:
            dis_list.append(False)
    return all(dis_list)


def load_pista(request):
    club_id =request.GET.get('id_club')
    print(club_id)
    pistas= Pistas.objects.filter(club__id=club_id)
    
    #return render(request,'option.html',{'pistas':pistas})
    return JsonResponse(list(pistas.values('id','nombre')), safe=False)

def load_hora(request):
    club_id =request.GET.get('id_club')
    
    horas= Hora.objects.filter(club__id=club_id)
    
    #return render(request,'option.html',{'pistas':pistas})
    return JsonResponse(list(horas.values('id','hora')), safe=False)
    
        
        

def re(request):
    
    
    data ={
        'form': DisponibleForm()
    }
    
   
        
   
    if request.method == 'POST':
        formulario =DisponibleForm(data=request.POST)
        if formulario.is_valid():
            pista_list = Pistas.objects.all()
            disponible_pista=[]
            for pista in pista_list:
                if mirar_disponibilidad(formulario.cleaned_data['pista'], formulario.cleaned_data['fecha'],formulario.cleaned_data['hora']):
                    disponible_pista.append(pista)

            if len(disponible_pista)>0:
                pista= disponible_pista[0]
                reserva= Reservas.objects.create(
                user = request.user,
                nombre= formulario.cleaned_data['nombre'],
                club=formulario.cleaned_data['club'],
                pista = formulario.cleaned_data['pista'],
                fecha = formulario.cleaned_data['fecha'],
                hora = formulario.cleaned_data['hora']
                )
                
                reserva.save()
                data["mensaje"]="Reservado  con exito!"
                
                
                #asunto = 'Reserva de reserpadel'
                #mensaje1 ="Nombre: "+formulario.cleaned_data['nombre']+" Club: "+clubs.values('nombre')+" Pista: "+ formulario.cleaned_data['pista']+" Fecha: "+ formulario.cleaned_data['fecha']+" Hora: "+ formulario.cleaned_data['hora']
                #email_from = settings.EMAIL_HOST_USER
                #recipent_list=[request.user.email]
                #send_mail(asunto,mensaje1,email_from,recipent_list)

            else:
                 
                return render(request,'nodispo.html',data)

        else:
            data["form"] = formulario
            return render(request,'nodispo.html',data)
        data["mensaje"]="Reservado  con exito!"
    return render(request,'disponible_form.html',data)
       




       



class Pistalista(generic.ListView):
    model= Pistas
    
    
    def get_queryset(self):
        texto= self.request.GET.get('nombre')
        if texto:
            pista=Pistas.objects.filter(club__nombre__contains=texto)
        else:
            pista = Pistas.objects.all()
        return pista

class ReservaList(generic.ListView):
    model= Reservas 
    
    def get_queryset(self):
        if self.request.user.is_staff:
            texto= self.request.GET.get('fecha1')
            if texto:
                reserva_list=Reservas.objects.filter(fecha=texto).order_by('-fecha')
            else:
                reserva_list=Reservas.objects.all().order_by('-fecha')
            return reserva_list
        else:
            texto= self.request.GET.get('fecha1')
            if texto:
                reserva_list =Reservas.objects.filter(user=self.request.user,fecha=texto).order_by('-fecha')
            else:
                reserva_list =Reservas.objects.filter(user=self.request.user).order_by('-fecha')
            return reserva_list    
        


class PistaDetailView(generic.DetailView):
    model = Pistas

class ReservasDetailView(generic.DetailView):
    model = Reservas   

class Contactoslista(generic.ListView):
    model:Contacto

    def get_queryset(self):
        return Contacto.objects.order_by('id')

class ContactosDetailView(generic.DetailView):
    model:Contacto

    def get_queryset(self):
        return Contacto.objects.order_by('id')

def eliminarreserva(request,id):
    reservas=Reservas.objects.get(pk=id)
    reservas.delete()
    return redirect('reserva-detail')
    

class UserprofileView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = UserProfile
    template_name = 'perfil.html'
    success_url = reverse_lazy('index')
    
    def get_object(self, queryset=None):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name= 'password.html'
    success_url = reverse_lazy('password_success')
    

def password_success(request):
    return render (request, 'password_success.html',{})


