from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import VacinasForm
from .models import Vacinas

from CadastroDePessoa.models import Usuario



@login_required(redirect_field_name='index_login')
def vacinas(request):
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user.id)
    dados_vacinas = Vacinas.objects.filter(fk_usuario_vacinas=usuario.id_usuario)

    if str(request.method) == 'POST':
        form = VacinasForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('vacinas')
            
    return render(request, "vacinas.html",
        {
            'dados_user': usuario,
            'dados_vacinas': dados_vacinas
        })


@login_required(redirect_field_name='index_login')
def vacinas_detail(request, pk):
    usuario = get_object_or_404(Usuario, id_fk_cadastro_user=request.user.id)
    dados_vacinas = Vacinas.objects.filter(fk_usuario_vacinas=usuario.id_usuario)
    
    vacina_detail = get_object_or_404(Vacinas, id_vacinas=pk)

    if str(request.method) == 'POST':
        form = VacinasForm(request.POST, instance=vacina_detail)
        if form.is_valid():
            form.save()
            return redirect("vacinas")
            
    return render(request, "vacinas.html",
        {
            'dados_user': usuario,
            'dados_vacinas': dados_vacinas,
            'vacina_detail': vacina_detail
        })


@login_required(redirect_field_name='index_login')
def delete_vacina(request, pk):
    vacina = get_object_or_404(Vacinas, id_vacinas=pk)
    vacina.delete()

    return redirect('vacinas')


