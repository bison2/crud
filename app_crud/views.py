from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pessoa
from django.contrib.auth.models import  User
from django.forms import ModelForm


# Create your views here.

class PessoaForm(ModelForm):
   class Meta:
      model = Pessoa
      fields = ['nome','slug']


def lista_pessoas(request):
    lista = Pessoa.objects.all().order_by('nome')
    print(lista)
    print(request.user)
    context = {
                'pessoas': lista,
                'user': request.user,            
             }
    return render(request, "app_crud/lista.html", context)

def pessoa_id(request, id):
   obj = Pessoa.objects.get(id=id)
   #return HttpResponse("<h1>a pessoa é {}</h1>".format(obj.nome))
   context = {
               'pessoa':obj,
               }
   return render(request, 'app_crud/detail.html', context)


def delete(request, id):
   obj = Pessoa.objects.get(id=id)
   print(obj.id, obj.nome, obj.slug)
   
   context = {
               'pessoa':obj.nome,
               'pessoa_id':obj.id               
               }
   obj.delete()
   return render(request, 'app_crud/delete.html', context)
   #return HttpResponse('<h1> O objeto {} foi deletado</h1>'.format(obj.nome))

def editar(request,id):
   obj = Pessoa.objects.get(id=id)
   print(obj.id, obj.nome, obj.slug)
   Pessoa.objects.filter(id=obj.id).update(nome='Alemanha', slug='nazista e racista')
   
   context = {
               'pessoa':obj.nome,
               'pessoa_id':obj.id,
               'pessoa_slug':obj.slug
               }
   
   return render(request, 'app_crud/edite.html', context)

   #return HttpResponse('<h1> O objeto foi alterado. Seu novo nome é {} , e seu slug é {}</h1>'.format(obj.nome, obj.slug))
   
def criar_pessoa(request):
   obj = Pessoa.objects.create(nome='Aristóteles', slug='estoicismo para viver.')

   context = {
               'pessoa':obj
               }
   return render(request, 'app_crud/criar.html', context)
    #return HttpResponse('<h1>O objeto {} foi criado. Seu id é {}, e seu slug é {}</h1>'.format(obj.nome, obj.id, obj.slug))
