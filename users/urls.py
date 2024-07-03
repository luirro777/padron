#
from django.urls import path

from . import views

app_name = "users_app"


urlpatterns = [   
    path(
        'login/', 
        views.LoginUser.as_view(),
        name='user-login',
    ),
    path(
        'logout/', 
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    path(
        'panel/', 
        views.Panel.as_view(), 
        name='user-panel'
    ),
    path(
        'lista-mesas/', 
        views.MesaListView.as_view(), 
        name='lista-mesas'
    ),
    path(
        'detalle-mesa/<pk>/', 
        views.MesaDetailView.as_view(), 
        name='detalle-mesa'
    ),
    path(
        'padron/<numero>/', 
        views.PadronMesaListView.as_view(), 
        name='padron-por-mesa'
    ),   
    path(
        'padronpdf/<numero>/', 
        views.PadronMesaListViewPdf.as_view(), 
        name='padronpdf-por-mesa'
    ), 
    path(
        'padrontotal/', 
        views.PadronListView.as_view(), 
        name='padron-total'
    ),    
]