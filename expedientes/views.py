from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona, Archivo
from .forms import ArchivoForm

# Create your views here.

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'expedientes/lista_personas.html', {'personas': personas})

def detalle_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    archivos = persona.archivos.all()

    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.save(commit=False)
            archivo.persona = persona
            archivo.nombre_original = archivo.archivo.name
            archivo.save()
            return redirect('detalle_persona', persona_id=persona.id)
    else:
        form = ArchivoForm()

    return render(request, 'expedientes/detalle_persona.html', {
        'persona': persona,
        'archivos': archivos,
        'form': form,
    })

