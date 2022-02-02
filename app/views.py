from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import *

def listar_veiculo(request, categoria, template_name="veiculo_list.html"):
    query = request.GET.get("busca", '')
    page = request.GET.get('page', '')
    ordenar = request.GET.get("ordenar", '')
    if query:
        veiculo = Veiculo.objects.filter(modelo__icontains=query, tipo=categoria)
    else:
        try:
            if categoria != "todos":
                if ordenar:
                    veiculo = Veiculo.objects.filter(tipo=categoria).order_by(ordenar)
                else:
                    veiculo = Veiculo.objects.filter(tipo=categoria)
            else:
                if ordenar:
                    veiculo = Veiculo.objects.all().order_by(ordenar)
                else:
                    veiculo = Veiculo.objects.all()
            veiculo = Paginator(veiculo, 1)
            veiculo = veiculo.page(page)
        except PageNotAnInteger:
            veiculo = veiculo.page(1)
        except EmptyPage:
            veiculo = paginator.page(paginator.num_pages)
    veiculos = {'lista': veiculo}
    return render(request, template_name, veiculos)

def perfil_veiculo(request, pk, template_name="perfil_veiculo.html"):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    return render(request, template_name, {'veiculo': veiculo})
