import nltk
import re

# Descargar recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('stopwords')

def tokenizar_texto(texto, 
                    eliminar_stopwords=False, 
                    eliminar_puntuacion=False, 
                    convertir_minusculas=True):
    """
    Función para tokenizar un texto con opciones de preprocesamiento.
    
    Parámetros:
    - texto (str): Texto a tokenizar
    - eliminar_stopwords (bool): Eliminar palabras vacías (por defecto: False)
    - eliminar_puntuacion (bool): Eliminar signos de puntuación (por defecto: False)
    - convertir_minusculas (bool): Convertir a minúsculas (por defecto: True)
    
    Retorna:
    - list: Lista de tokens
    """
    # Convertir a minúsculas si está habilitado
    if convertir_minusculas:
        texto = texto.lower()
    
    # Tokenización usando NLTK
    tokens = nltk.word_tokenize(texto)
    
    # Eliminar puntuación si está habilitado
    if eliminar_puntuacion:
        tokens = [token for token in tokens if token.isalnum()]
    
    # Eliminar stopwords si está habilitado
    if eliminar_stopwords:
        stopwords = set(nltk.corpus.stopwords.words('spanish'))
        tokens = [token for token in tokens if token not in stopwords]
    
    return tokens
