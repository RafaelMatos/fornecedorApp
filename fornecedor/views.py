from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Fornecedor,Produto
from django.urls import reverse
# from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'fornecedor/index.html'
    context_object_name = 'all_fornecedores'
    def get_queryset(self):
        return Fornecedor.objects.all().order_by("nome")

class DetailView(generic.DetailView):
    model = Fornecedor
    template_name = 'fornecedor/detail.html'

class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = ['CNPJ','nome','is_ativo']

class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = ['CNPJ','nome','is_ativo']

class FornecedorDelete(DeleteView):
    model = Fornecedor
    success_url = reverse('fornecedor:index')
    # def get_success_url():
    #     return reverse('fornecedor:index')
