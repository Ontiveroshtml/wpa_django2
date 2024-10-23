from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import os
import json

def manifest(request):
    # Ruta absoluta al archivo manifest.json (ajusta según la estructura de tu proyecto)
    manifest_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'manifest.json')
    
    try:
        # Lee el archivo y devuelve su contenido como JSON
        with open(manifest_path, 'r', encoding='utf-8') as f:
            data = json.load(f)  # Carga el archivo como JSON
        
        # Devuelve la respuesta JSON
        return JsonResponse(data, safe=False)
    
    except FileNotFoundError:
        # Si el archivo no se encuentra, devuelve un error 404
        return HttpResponse("Archivo manifest.json no encontrado", status=404)
    
    except json.JSONDecodeError:
        # Si hay un error en el formato del JSON, devuelve un error 500
        return HttpResponse("Error al decodificar manifest.json", status=500)
    
def serviceworker(request):
    return render(request, "principal/serviceworker.js", {}, content_type="text/javascript")

# Create your views here.
def index(request):
    return render(request, "principal/index.html",{})

def detail(request, question_id):
    return HttpResponse("Estas viendo una pregunta %s." % question_id)

def result(request, question_id):
    response = "Estas viendo las respuestas de la pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Tu estas votando en la pregunta %s." % question_id)