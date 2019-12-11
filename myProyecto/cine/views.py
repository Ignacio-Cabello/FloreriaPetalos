from django.shortcuts import render, redirect
from .models import Pelicula #importar los modelos desde el archivo models.py 
from .forms import CustomUserForm, FlorForm
 #definir los metodos con un login requerido
from django.contrib.auth.decorators import login_required, permission_required
#debemos incluir el modelo de users del sistema
from django.contrib.auth.models import User
#incluimos el sistema de autentificacion de Django, 
#le di un alias a 'login'
from django.contrib.auth import authenticate,logout, login as auth_login
# Create your views here.

def home(request):
    return render(request, 'core/index.html')

def galeria(request):
    return render(request, 'core/galeria.html')

@login_required(login_url='/login/')
def listado_flores(request):
    flores = Pelicula.objects.all()
    data = {
        'flores':flores
    }
    return render(request, 'core/listado_flores.html',data)

@login_required(login_url='/login/')
def nueva_flor(request):
    data = {
        'form':FlorForm()
    }

    if request.method == 'POST':
        formulario = FlorForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
        data['form'] = formulario

    return render(request, 'core/nueva_flor.html',data)

def modificar_flores(request,id):
    flor = Pelicula.objects.get(name=id)
    data = {
        'form': FlorForm(instance=flor)
    }
    
    if request.method == 'POST':
        formulario = FlorForm(data=request.POST, instance=flor) #files=request.FILES
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
            data['form'] = formulario #FlorForm(instance=flor.objects.get(name=id))
    return render(request, 'core/modificar_flores.html',data)

def eliminar_flor(request, id):
    flor = Pelicula.objects.get(name=id)
    flor.delete()

    return redirect(to="listado_flores")

def registro_usuario(request):

    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='GAL')

    return render(request, 'registration/registrar.html', data)

def agregar_carrito(request,id):
    #recuperar la lista del carrito desde la sesion
    lista=request.session.get("carrito","")
    #agregar el titulo a listado
    lista=lista+str(id)+str(";")
    #volver a ingresarlo a la sesion
    request.session["carrito"]=lista
    return render(request,"core/carrito.html",{'listaCarrito':lista})

def eliminar_pelicula(request,id):
    peli=Pelicula.objects.get(name=id)#buscar pelicula
    msg=''
    try:
        peli.delete()# elimino
        msg='Elimino Pelicula'
    except:
        msg='No elimino'
    lPelis=Pelicula.objects.all()# selecciono todo
    return render(request,"core/galeria.html",{'lista':lPelis,'msg':msg})
    

def login(request):
    return render(request,"core/login.html")

def cerrar_sesion(request):
    logout(request)
    return render(request,"core/login.html",{'msg':'cerro sesion'})
    
def login_acceso(request):
    if request.POST:
        usuario=request.POST.get("txtUser")
        password=request.POST.get("txtPass")
        #creamos un modelo de usuario para autentificar
        us = authenticate(request,username=usuario,password=password)
        if us is not None and us.is_active:
            auth_login(request,us)
            return render(request,"core/index.html")
    return render(request,"core/login.html",{'msg':'jaja'})

@login_required(login_url='/login/')
def index(request):
    return render(request,'core/index.html')

@login_required(login_url='/login/')
def gale(request):
    pelis=Pelicula.objects.all()#select * from Peliculas
    return render(request,'core/galeria.html',{'lista':pelis})

@login_required(login_url='/login/')
def formulario(request):
    categorias=Categoria.objects.all() # select * form Categoria
    if request.POST:
        # recuperar el valor del boton accion
        accion=request.POST.get("accion")
        if accion=='grabar':            
            titulo=request.POST.get("txtTitulo")
            precio=request.POST.get("txtPrecio")
            duracion=request.POST.get("txtDuracion")
            descrip=request.POST.get("txtDescripcion")
            catego=request.POST.get("cboCategoria")
            imagen=request.FILES.get("txtImagen")
            obj_categoria=Categoria.objects.get(name=catego)
            #instanciar un objeto (modelo) Pelicula
            peli=Pelicula(
                name=titulo,
                precio=precio,
                duracion=duracion,
                descripcion=descrip,
                imagen=imagen,
                categoria=obj_categoria
            )
            peli.save() #graba los datos del modelo
            return render(request,'core/formulario.html',{'listacategoria':categorias,'msg':'grabo'})
        if accion=='eliminar':
            titulo=request.POST.get("txtTitulo")#recupera el titulo
            peli=Pelicula.objects.get(name=titulo)# lo busca entre las peliculas
            peli.delete()#elimina
            return render(request,'core/formulario.html',{'listacategoria':categorias,'msg':'elimino'})
    return render(request,'core/formulario.html',{'listacategoria':categorias})

@login_required(login_url='/login/')
def quienes_somos(request):
    return render(request,'core/quienes_somos.html')