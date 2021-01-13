from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'exm1'
urlpatterns = [
    #path('criar/', views.criar_pessoa, name='criar'),
    url(r'^criar$', views.criar_pessoa, name='criar'),
    path('', views.lista_pessoas, name ='listas'),
   # path('<int:id>', views.pessoa_id, name='pessoa'),
    url(r'^detail/(?P<id>\d+)$', views.pessoa_id, name='pessoa'),
    #path('<int:id>/editar/', views.editar, name='editar'),
    url(r'^editar/(?P<id>\d+)$', views.editar, name='editar'),
    #path('<int:id>/delete/', views.delete, name='delete'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),

  
]
    