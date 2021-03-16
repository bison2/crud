from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Pessoa
from django.contrib.auth.models import  User
from django.forms import ModelForm
from django.urls import reverse
#from urllib3 import request

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
   #return reverse('app_crud:detalhe', kwargs={'id':'self.id'})
   #return HttpResponseRedirect(reverse('app_crud:detalhe', args=[id])) 

def delete(request, id):
   #obj = Pessoa.objects.get(id=id)
   #print(obj.id, obj.nome, obj.slug)
   #context = {
    #           'pessoa':obj.nome,
     #          'pessoa_id':obj.id               
      #         }
   #obj.delete()
   #return render(request, 'app_crud/delete.html', context)
   #return HttpResponse('<h1> O objeto {} foi deletado</h1>'.format(obj.nome))

   person = get_object_or_404(Pessoa, id=id)
   if request.method=='POST':
      person.delete()
      return redirect('app_crud:listas')
   return render(request, 'app_crud/delete.html',{'object':person})

def editar(request,id):
   #obj = Pessoa.objects.get(id=id)
   #print(obj.id, obj.nome, obj.slug)
   #Pessoa.objects.filter(id=obj.id).update(nome='Alemanha', slug='nazista e racista')
   #context = {
    #           'pessoa':obj.nome,
     #          'pessoa_id':obj.id,
      #         'pessoa_slug':obj.slug
       #        }
   #return render(request, 'app_crud/edite.html', context)
   #return HttpResponse('<h1> O objeto foi alterado. Seu novo nome é {} , e seu slug é {}</h1>'.format(obj.nome, obj.slug))
   person = get_object_or_404(Pessoa, id=id)
   form = PessoaForm(request.POST or None, instance=person)
   if form.is_valid():
      form.save()
      return redirect('app_crud:listas')
   return render(request,'app_crud/edite.html', {'form':form})

def criar_pessoa(request):
   #obj = Pessoa.objects.create(nome='Aristóteles', slug='estoicismo para viver.')
   #context = {
    #           'pessoa':obj
     #          }
   #return render(request, 'app_crud/criar.html', context)
    #return HttpResponse('<h1>O objeto {} foi criado. Seu id é {}, e seu slug é {}</h1>'.format(obj.nome, obj.id, obj.slug))
   form = PessoaForm(request.POST or None)
   if form.is_valid():
      form.save()
      return redirect('app_crud:listas')
   return render(request, 'app_crud/criar.html', {'form':form})