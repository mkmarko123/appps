from django.urls import path
from hule import views


app_name = 'hule'


urlpatterns = [
    path('home/<int:usuario_id>/', views.home, name='home'), # ve todas sus fincas que le corresponden

    path('crear/<int:usuario_id>/', views.crear_finca, name='crear_finca'),     # crea una su finquita
    path('editar/<int:finca_id>/', views.editar_finca, name='editar_finca'),    # edita su finquita
    path('borrar/<int:finca_id>/', views.borrar_finca, name='borrar_finca'),    # elimina su finquita

    path('home-p/<int:usuario_id>/', views.home_parcelas, name='home_parcelas'),    # ve todas sus parcelas
    path('ver/<int:usuario_id>/<int:finca_id>/', views.ver_parcela_de_finca, name='ver_parcela'),   # ver parcelas
    path('crear-p/<int:usuario_id>/<int:finca_id>/', views.nueva_parcela, name='crear_parcela'),    # crear parcela
    path('editar-p/<int:usuario_id>/<int:finca_id>/', views.editar_parcela, name='editar_parcela'),    # crear parcela

    path('arboles/', views.arboles, name='arboles'),
]