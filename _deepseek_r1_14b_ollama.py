"""
Módulo para la implementación del modelo DeepSeek-R1 utilizando Ollama.
"""

import re
from ollama import Client

# Crear cliente Ollama
client = Client(host='http://localhost:11434')


def remove_think_tags(text: str) -> str:
    """
    Elimina las etiquetas <think> y su contenido del texto generado.
    
    Args:
        text (str): Texto que puede contener etiquetas <think>
        
    Returns:
        str: Texto limpio sin etiquetas <think> ni su contenido
    """
    resultado = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    resultado = resultado.replace("</think>", "")
    resultado = resultado.replace("<think>", "")
    return resultado


def generate_response(pregunta: str, texto: str) -> str:
    """
    Genera una respuesta utilizando el modelo DeepSeek-R1 a través de Ollama.
    
    Args:
        pregunta (str): Texto de entrada para generar la respuesta
        texto (str): Texto de contexto para generar la respuesta
        
    Returns:
        str: Respuesta generada y procesada por el modelo
    """
    prompt = (
        f"Se te proporciona una pregunta que es esta: {pregunta}. "
        f"Tambien se te proporciona un texto que es este: {texto}. "
        "Responde a la pregunta con el texto proporcionado. "
        "Tu tarea es responder con la mayor claridad, precisión y concisión "
        "posible en base al texto proporcionado. El formato debe seguir el "
        "estandar de markdown. El lenguaje debe ser formal. "
        "Independientemente del idioma del texto, la respuesta has de "
        "devolverla en español."
    )
    response = client.generate(
        model='deepseek-r1:7b',
        prompt=prompt,
        options={
            'num_ctx': 20000
        }
    )
    response = response['response']
    response = remove_think_tags(response)
    
    return response.strip()
