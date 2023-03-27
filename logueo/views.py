from django.shortcuts import render, redirect
from logueo.models import usuario, informacion


# Create your views here.
def home(request):
    return render(request, "login.html", {})

def loginsesiondef(request):
    if request.method == 'GET':
        return render(request,"login.html",{})
    else:
        usustr = request.POST.get('usu')
        passtr = request.POST.get('pass')
        try:
            print(usustr, passtr)
            usu=usuario.objects.get(usuario=usustr, password=passtr)
            print(usustr, passtr)
            infousulist = informacion.objects.get(usuario=usu)
            return render(request, "bienvenido.html", {
                'usuid': usu.id,
                'usu': usu.usuario,
                'usues': usu.estado,
                "infousuid": infousulist.id,
                "infousuci": infousulist.ci,
                "infousunom": infousulist.nombre,
                "infousuape": infousulist.apellido,
                "infousufech": infousulist.fcha_nacimiento,
                "infousudir": infousulist.direccion,
                "infousuema": infousulist.email
            })
        except usuario.DoesNotExist:
            return render(request, "login.html",{"err":"-Usuario y contraseña incorrectos-"})
#
def regissesiondef(request):
    if request.method == 'POST':
        idstr = request.POST.get('idnew')
        usustr = request.POST.get('usenew')
        passtr = request.POST.get('passnew')
        estado = request.POST.get('estado', True)
        idnew = request.POST.get('idusu')
        cinew = request.POST.get('ciusu')
        nomnew = request.POST.get('nomusu')
        apenew = request.POST.get('apeusu')
        datenew = request.POST.get('dateusu')
        direnew = request.POST.get('direusu')
        imenew = request.POST.get('imeusu')
        usuarios = usuario(
            id=idstr,usuario=usustr,password=passtr,estado=estado)
        usuarios.save()
        usuario_instancia = usuario.objects.get(id=idstr)
        informacionu = informacion(
            id=idnew, ci=cinew, nombre=nomnew, apellido=apenew, fcha_nacimiento=datenew,
            direccion=direnew, email=imenew, usuario=usuario_instancia)
        informacionu.save()
        return redirect('/')