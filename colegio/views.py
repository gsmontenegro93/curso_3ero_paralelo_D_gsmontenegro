from django.db.models import Q
from django.shortcuts import render, redirect
from colegio.models import curso,estudiante
from django.contrib import messages
# Create your views here.
def home(request):
    proveedores = curso.objects.all()
    messages.success(request, '¡Cursos listados!')
    productos = estudiante.objects.all()
    messages.success(request, '¡Estudiantes listados!')
    return render(request, "gestion.html", {"proveedores":proveedores,
                                                    "productos": productos
                                                    })
def registroproveedor(request):
    proveid= request.POST['txtid']
    provenom= request.POST['txtNombre']
    provedire= request.POST['txtdire']
    provetelef= request.POST['txtele']

    proovedores = curso.objects.create(id=proveid,
                                           nombre=provenom,
                                           direccion=provedire,
                                           telefono=provetelef)
    messages.success(request, '¡Cursos listados!')
    return redirect('gestion_producto')

def registroproducto(request):
    producid= request.POST['txtidpro']
    producnombre= request.POST['txtNombrepro']
    producdescri= request.POST['txtdescrippro']
    proveeid = request.POST['txtidproovee']
    productos = estudiante.objects.create(id=producid,
                                          nombre=producnombre,
                                          materia=producdescri,
                                        curso_id=proveeid)
    messages.success(request, '¡Estudiante Registrado!')
    return redirect('gestion_producto')


def eliminarproveedor(request,id):
    proves = curso.objects.get(id=id)
    proves.delete()
    messages.success(request, '¡Curso Eliminado!')
    return redirect('gestion_producto')

def eliminarproducto(request,id):
    proves = estudiante.objects.get(id=id)
    proves.delete()
    messages.success(request, '¡Estudiante Eliminado!')
    return redirect('gestion_producto')

def editarproveedor(request,id):
    proves = curso.objects.get(id=id)
    return render(request,"editc.html",{"editprove":proves})

def guardaredicioproveedor(request):
    proveid = request.POST['txtid']
    provenom= request.POST['txtNombre']
    provedire= request.POST['txtdire']
    provetelef= request.POST['txtele']

    proves = curso.objects.get(id=proveid)
    proves.nombre = provenom
    proves.direccion = provedire
    proves.telefono = provetelef
    proves.save()
    messages.success(request, '¡Curso Actualizados!')

    return redirect('gestion_producto')

def editarproducto(request,id):
    producs = estudiante.objects.get(id=id)
    return render(request,"edite.html",{"editproduc":producs})

def guardaredicioproducto(request):
    produid = request.POST['txtidpro']
    produnom= request.POST['txtNombrepro']
    produdesc= request.POST['txtdescrippro']


    produc = estudiante.objects.get(id=produid)
    produc.nombre = produnom
    produc.materia = produdesc
    produc.save()
    messages.success(request, '¡Estudiante Actualizado!')

    return redirect('gestion_producto')