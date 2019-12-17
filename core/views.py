from django.shortcuts import render,redirect
from .models import Cliente, Ordentrabajo,Tecnico
from .forms import ClienteForm ,OrdentrabajoForm,TecnicoForm,CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login,authenticate

# Create your views here.

def index(request):

    return render(request, 'core/index.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def galeria(request):
    data = {
        'tecnicos': Tecnico.objects.all()
    }

    return render(request, 'core/galeria.html',data)
@permission_required('core.view_cliente')
def listado_cliente(request):
    clientes = Cliente.objects.all()
    data = {
        'clientes' : clientes
    }
    return render(request, 'core/listado_clientes.html', data)

def nuevo_cliente(request):
    data = {
        'form':ClienteForm()
    }

    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
    return render(request, 'core/nuevo_cliente.html', data)

def modificar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    data = {
        'form':ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST,instance=cliente)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario

    return render(request, 'core/modificar_cliente.html',data)


def eliminar_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()

    return redirect(to='listado_clientes')

@permission_required('core.view_ot')
def listado_ot(request):
    ordentrabajos = Ordentrabajo.objects.all()
    data = {
        'ordentrabajos' : ordentrabajos
    }
    return render(request, 'core/listado_ot.html', data)

def modificar_ot(request, id):
    ordentrabajo = Ordentrabajo.objects.get(id=id)

    data = {
        'form':OrdentrabajoForm(instance=ordentrabajo)
    }
    if request.method == 'POST':
        formulario = OrdentrabajoForm(data=request.POST,instance=ordentrabajo)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = formulario

    return render(request, 'core/modificar_ot.html',data)

@permission_required('core.add_ot')
def nuevo_ot(request):
    data = {
        'form':OrdentrabajoForm()
    }

    if request.method == 'POST':
        formulario = OrdentrabajoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
    return render(request, 'core/nuevo_ot.html', data)

def eliminar_ot(request,id):
    ordentrabajo = Ordentrabajo.objects.get(id=id)
    ordentrabajo.delete()

    return redirect(to='listado_ot')

@permission_required('core.add_tecnico')
def nuevo_tecnico(request):
    data = {
        'form':TecnicoForm()
    }

    if request.method == 'POST':
        formulario = TecnicoForm(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
    return render(request, 'core/nuevo_tecnico.html', data)

def modificar_tecnico(request, id):
    tecnico = Tecnico.objects.get(id=id)

    data = {
        'form':TecnicoForm(instance=tecnico)
    }
    if request.method == 'POST':
        formulario = TecnicoForm(data=request.POST,instance=tecnico, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
            data['form'] = TecnicoForm(instance=Tecnico.objects.get(id=id))

    return render(request, 'core/modificar_tecnico.html',data)
@permission_required('core.view_tecnico')
def listado_tecnico(request):
    tecnico = Tecnico.objects.all()
    data = {
        'tecnico' : tecnico
    }
    return render(request, 'core/listado_tecnico.html', data)

def eliminar_tecnico(request,id):
    tecnico = Tecnico.objects.get(id=id)
    tecnico.delete()

    return redirect(to='listado_tecnico')

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='index')


    return render(request,'registration/registrar.html',data)

