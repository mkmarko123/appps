from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from hule.models import Finca, Parcela, Tree
from usuario.models import Usuario


# Create your views here.
def home(request, usuario_id):
    template = 'hule/home.html'
    context = {
        'fincas': Finca.objects.filter(propietario_id=usuario_id),
        'usuario': usuario_id,
        'usuarios': Usuario.objects.filter(pk=usuario_id),
        'parcela_id': usuario_id,
    }
    return render(request, template, context)


def crear_finca(request, usuario_id):
    if request.method == 'POST':
        nueva_finca = Finca(
            nombre=request.POST['nombre'],
            pais=request.POST['pais'],
            departamento=request.POST['departamento'],
            propietario_id=request.POST['propietario_id'],
        )
        nueva_finca.save()

        return HttpResponseRedirect(reverse('hule:home', kwargs={'usuario_id': nueva_finca.propietario.id}))
    elif request.method == 'GET':
        template = 'hule/crear_finca.html'
        context = {
            'usuario': usuario_id
        }
        return render(request, template, context)
    return HttpResponse('Error al procesarlos datos')


def editar_finca(request, finca_id):
    if request.method == 'POST':
        update_finca = Finca.objects.get(id=finca_id)
        update_finca.nombre = request.POST['nombre']
        update_finca.pais = request.POST['pais']
        update_finca.departamento = request.POST['departamento']
        update_finca.save()

        return HttpResponseRedirect(reverse('hule:home', kwargs={'usuario_id': update_finca.propietario.id}))
    elif request.method == 'GET':
        template = 'hule/editar_finca.html'
        context = {
            'finca': Finca.objects.get(id=finca_id)
        }
        return render(request, template, context)
    return HttpResponse('Error al analisar.')


def borrar_finca(request, finca_id):
    eliminar_finca = Finca.objects.get(id=finca_id)
    eliminar_finca.delete()

    return HttpResponseRedirect(reverse('hule:home', kwargs={'usuario_id': eliminar_finca.propietario.id}))


# ------------------------------------------------------------------------------------------------------------------------------


def home_parcelas(request, usuario_id):
    template = 'hule/home_parcelas.html'
    context = {
        'parcelas': Parcela.objects.all(),
        'usuario_id': usuario_id,
        'cant_parcelas': Parcela.objects.count(),
    }
    return render(request, template, context)


def ver_parcela_de_finca(request, usuario_id, finca_id):
    template = 'hule/ver_parcelas.html'
    context = {
        'parcelas': Parcela.objects.all(),
        'usuario_id': usuario_id,
        'cant_parcelas': Parcela.objects.count(),
        'finca': Finca.objects.get(pk=finca_id),
    }
    return render(request, template, context)


def nueva_parcela(request, usuario_id, finca_id):
        if request.method == 'POST':
            crear_parcela = Finca(
                finca_origen=Finca.objects.get(pk=request.POST['finca_origen']),
                nombre=request.POST['nombre'],
                latitud=request.POST['latitud'],
                longitud=request.POST['longitud'],
            )
            crear_parcela.save()

            return HttpResponseRedirect(reverse('hule:home', kwargs={'usuario_id': usuario_id, 'finca_id': finca_id}))
        elif request.method == 'GET':
            template = 'hule/crear_parcela.html'
            context = {
                'finca': Finca.objects.get(pk=finca_id),
                'usuario': Usuario.objects.get(pk=usuario_id)
            }
            return render(request, template, context)
        return HttpResponse('No se puede guardar!!!')


def editar_parcela(request, usuario_id, finca_id):
    if request.method == 'POST':
        update_parcela = Finca.objects.get(pk=request.POST['finca_origen'])
        update_parcela.nombre = request.POST['nombre']
        update_parcela.latitud = request.POST['latitud']
        update_parcela.longitud = request.POST['longitud']
        update_parcela.save()

        return HttpResponseRedirect(reverse('hule:home', kwargs={'usuario_id': usuario_id, 'finca_id': finca_id}))
    elif request.method == 'GET':
        template = 'hule/editar_parcela.html'
        context = {
            'finca': Finca.objects.get(pk=finca_id),
            'usuario': Usuario.objects.get(pk=usuario_id)
        }
        return render(request, template, context)
    return HttpResponse('Error al analisar.')


def arboles(request):
    cant_arbol = Tree.objects.count()
    print(cant_arbol)
    if cant_arbol < 10:
        return HttpResponse('bien')
    else:
        return HttpResponse('mal')
