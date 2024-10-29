from django.shortcuts import render
from .utils.bedrock_utils import BedrockClient

def home(request):
    return render(request, 'generadores/home.html')

def generador_metadata(request):
    if request.method == 'POST':
        url = request.POST.get('urls')
        keyword = request.POST.get('keyword')
        
        # Crear instancia del cliente de Bedrock
        bedrock_client = BedrockClient()
        
        # Generar metadatos solo si se seleccionaron las opciones correspondientes
        if any([request.POST.get('meta_title'), 
                request.POST.get('meta_description'),
                request.POST.get('h1')]):
            
            metadata = bedrock_client.generate_seo_metadata(url, keyword)
            
            if metadata:
                context = {
                    'meta_title': metadata.get('meta_title') if request.POST.get('meta_title') else None,
                    'meta_description': metadata.get('meta_description') if request.POST.get('meta_description') else None,
                    'h1': metadata.get('h1') if request.POST.get('h1') else None,
                }
                return render(request, 'generadores/generador_metadata.html', context)
            
            # Si hubo un error en la generación
            context = {'error': 'Hubo un error al generar los metadatos. Por favor, intente nuevamente.'}
            return render(request, 'generadores/generador_metadata.html', context)
    
    return render(request, 'generadores/generador_metadata.html')

#def generador_metadata(request):
#    return render(request, 'generadores/generador_metadata.html')

def generador_articulos(request):
    return render(request, 'generadores/generador_articulos.html')

def generador_datos(request):
    return render(request, 'generadores/generador_datos.html')
