from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona, Archivo
from .forms import ArchivoForm, PersonaForm

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

def nueva_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'expedientes/nueva_persona.html', {'form': form})

def editar_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('detalle_persona', persona_id=persona.id)
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'expedientes/editar_persona.html', {'form': form, 'persona': persona})
