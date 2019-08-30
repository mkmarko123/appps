from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from usuario.models import Usuario


# Create your views here.
def crear_usuario(request):
    if request.method == 'POST':
        nuevo_usuario = Usuario(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            telefono=request.POST['telefono'],
            correo=request.POST['correo'],
            clave=request.POST['clave'],
            permiso=request.POST['permiso'],
        )
        nuevo_usuario.save()

        return HttpResponseRedirect(reverse('usuario:inicio'))
    elif request.method == 'GET':
        template = 'usuario/crear_usuario.html'
        return render(request, template)
    return HttpResponse('Error en la solicitud.')


def inicio_sesion(request):
    if request.method == 'POST':
        try:
            usuario = Usuario.objects.get(correo=request.POST['correo'], clave=request.POST['clave'])
        except Usuario.DoesNotExist:
            return HttpResponseRedirect(reverse('usuario:inicio'))

        return HttpResponseRedirect(reverse('hule:home', kwargs={'usuario_id': usuario.id}))
    elif request.method == 'GET':
        template = 'usuario/inicio_usuario.html'
        return render(request, template)
    return HttpResponse('Error al procesar los datos.')


    """while True:
        error = 0

        usuario = input("Nombre de usuario ")
        pass1 = input("contrasena ")
        pass2 = input("repite contrasena ")

        if len(usuario) < 8 or len(usuario) > 12:
            print("la longitud del usuario no es correcta")
            error = 1
        if len(pass1) < 10:
            print("la longitud de la contrasena no es correcta")
            error = 1
        if not re.search('[0-9]', pass1):
            print("la contrasena tiene que tener al menos un numero")
            error = 1
        if pass1 != pass2:
            print("las contrasenas no son iguales")
            error = 1

        if error == 0:
            print("OK")
            break"""