"""
Módulo para sumarización de texto utilizando la API de Google Gemini.

Este módulo proporciona funcionalidad para:
- Generar resúmenes de texto usando el modelo Gemini
- Calcular costos asociados al uso de la API
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Cargar variables de entorno
load_dotenv()

def sumarizar_gemini(pregunta: str, texto: str) -> tuple[str, int, int, float]:
    """
    Genera un resumen de texto usando el modelo Gemini.

    Args:
        pregunta (str): Pregunta o contexto para guiar la sumarización
        texto (str): Texto a sumarizar

    Returns:
        tuple: Contiene:
            - str: Texto sumarizado o mensaje de error
            - int: Número de tokens de entrada
            - int: Número de tokens de salida
            - float: Costo estimado de la operación
    """
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-2.0-flash-exp")
        prompt = f"Se te proporcionaré una pregunta y un texto recopilado de diversas fuentes. Este texto puede estar desorganizado,fragmentado, y contener información redundante o irrelevante, ya que proviene de múltiples páginas web. Tu tarea es:\n1- Procesar el texto para limpiarlo, eliminar información irrelevante o duplicada, y estructurarlo de manera lógica y coherente.\n2- Utilizar este texto limpio y estructurado para responder de forma precisa, clara y concisa a la pregunta proporcionada.\nAsegúrate de basar tu respuesta únicamente en la información contenida en el texto procesado y no agregar datos externos. Indica si no encuentras información suficiente para responder la pregunta.\nPregunta:{pregunta}, Texto: {texto}"
        response = model.generate_content(prompt)
        input_tokens = model.count_tokens(prompt).total_tokens
        output_tokens = model.count_tokens(response.text).total_tokens
        cost = calculate_cost(input_tokens, output_tokens)
        print(f"Input tokens: {input_tokens}, Output tokens: {output_tokens}, Cost: {cost}")
        return f"{response.text}\n---\nInput tokens: {input_tokens}, Output tokens: {output_tokens}, Cost: {cost}", input_tokens, output_tokens, cost
    except:
        return "No pude responder la pregunta", 0, 0, 0

def calculate_cost(input_tokens: int, output_tokens: int) -> float:
    """
    Calcula el costo de uso de la API basado en tokens.

    Args:
        input_tokens (int): Número de tokens de entrada
        output_tokens (int): Número de tokens de salida

    Returns:
        float: Costo estimado en dólares
    """
    input_cost = 0.075 if input_tokens <= 128000 else 0.15
    output_cost = 0.30 if output_tokens <= 128000 else 0.60
    return (input_tokens / 1000000 * input_cost) + (output_tokens / 1000000 * output_cost)
