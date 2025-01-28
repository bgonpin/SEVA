"""
Módulo para extraer y procesar texto de páginas web.

Este módulo proporciona funcionalidad para:
- Cargar contenido HTML de URLs usando ChromiumLoader
- Transformar y extraer texto relevante usando BeautifulSoup
- Tokenizar y limpiar el texto extraído
"""

import os
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from _tokenizar import tokenizar_texto

if 'USER_AGENT' not in os.environ:
    os.environ['USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'


def extraer_texto(urls: list) -> str:
    """
    Extrae y procesa texto de una lista de URLs.

    Args:
        urls (list): Lista de URLs de las que extraer texto

    Returns:
        str: Texto procesado y tokenizado de todas las URLs,
             o cadena vacía si no se pudo extraer contenido
    
    Notas:
        - Ignora URLs que contengan 'msn'
        - Extrae contenido de etiquetas p, h1-h6 y li
        - El texto extraído es tokenizado y limpiado
    """
    texto_a_devolver = ""
    # Load HTML
    for url in urls:
        if "msn" in url:
            return False
        else:
            loader = AsyncChromiumLoader([url])
            html = loader.load()

            # Transform
            bs_transformer = BeautifulSoupTransformer()
            docs_transformed = bs_transformer.transform_documents(
                html, tags_to_extract=["p", "h1", "h2", "h3", "h4", "h5", "h6", "li"]
            )
            resultado = docs_transformed[0].page_content
            texto_a_devolver += resultado + " "
           
    # Tokenizamos todo el texto al final
    tokens = tokenizar_texto(texto_a_devolver, eliminar_stopwords=True, eliminar_puntuacion=True, convertir_minusculas=True)
    return " ".join(tokens) if tokens else ""
