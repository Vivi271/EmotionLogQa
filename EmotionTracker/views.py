from django.shortcuts import render, redirect
from .models import EmotionEntry
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io
import base64


def home_view(request):
    context = {
        'nav_options': ['Recursos', 'Libros', 'Videos', 'Coaching', 'Eventos'],
    }
    return render(request, 'EmotionTracker/home.html', context)


def emotion_entry_view(request):
    confirmation_message = None

    if request.method == 'POST':
        # Procesar el formulario de registro de emoción
        emotion_level = request.POST.get('emotion_level')
        user = request.POST.get('user')
        
        # Crear un nuevo registro de emoción en el modelo EmotionEntry
        emotion_entry = EmotionEntry(user=user, emotion_level=emotion_level)
        emotion_entry.save()
        
        # Agregar mensaje de confirmación
        confirmation_message = f"Emoción guardada: Usuario: {user}, Nivel de emoción: {emotion_level}"
        
    # Obtener las opciones para validar el progreso y volver al inicio
    options = {'validation_url': '/EmotionLog/ValidacionProgreso/', 'home_url': '/'}
    
    # Renderizar el formulario de registro de emoción utilizando el template específico
    return render(request, 'EmotionTracker/emotion_entry.html', {'confirmation_message': confirmation_message, 'options': options})


def progress_view(request):
    # Obtener los registros de emoción del usuario
    user = request.user  # Suponiendo que el usuario está autenticado
    emotion_entries = EmotionEntry.objects.filter(user=user)
    
    # Generar las gráficas
    fig, ax = plt.subplots()
    ax.plot([entry.date for entry in emotion_entries], [entry.emotion_level for entry in emotion_entries])
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Nivel de emoción')
    ax.set_title(f'Progreso emocional de {user}')  # Agregar el nombre del usuario como título
    
    # Convertir la gráfica a una imagen codificada en base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    
    context = {
        'emotion_chart': image_base64,
        'home_url': '/',  # Enlace para volver a la página de inicio
        'emotion_entry_url': '/EmotionLog/RegEmocion/',  # Enlace para registrar emociones
    }
    return render(request, 'EmotionTracker/progress.html', context)


def chatbot_view(request):
    return render(request, 'EmotionTracker/chatbot.html')
