"""
Módulo principal de la aplicación web para búsqueda y sumarización de contenido.

Este módulo implementa un servidor Flask que proporciona endpoints para:
- Realizar búsquedas en la web
- Extraer y sumarizar contenido
- Generar PDFs de los resultados
"""

# Imports estándar
import datetime
import io
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Imports de terceros
from flask import Flask, request, jsonify, render_template, send_file
from langchain_community.utilities import SearxSearchWrapper
import pymongo
import markdown
from xhtml2pdf import pisa

# Imports locales
from _raspar import extraer_texto
from _sumarizar import sumarizar_gemini

app = Flask(__name__)



def insertar_datos_mongodb(datos: dict) -> None:
    """
    Inserta los datos de una búsqueda en MongoDB.

    Args:
        datos (dict): Diccionario con los datos de la búsqueda a almacenar
    """
    try:
        client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
        db = client["miperplexity"]
        collection = db["busquedas"]
        collection.insert_one(datos)
    except Exception as e:
        print(f"Error al insertar datos en MongoDB: {e}")



def busqueda(query: str) -> list:
    """
    Realiza una búsqueda web utilizando SearxSearch.

    Args:
        query (str): Consulta de búsqueda

    Returns:
        list: Lista de resultados de la búsqueda
    """
    lista_resultado = []
    try:
        search = SearxSearchWrapper(
            searx_host=os.getenv("SEARX_URL"),
            headers={"User-Agent": "Mozilla/5.0"}
        )
        results = search.results(
            query,
            num_results = 10,
            languajes=["es", "en", "de", "fr", "it"],
        )
        for result in results:        
            lista_resultado.append(result)
            
        return lista_resultado
    except Exception as e:
        print(f"Error en la búsqueda: {e}")
        return []



@app.route('/')
def index() -> str:
    """Renderiza la página principal."""
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    """Sirve el favicon de la aplicación."""
    return send_file('templates/favicon.ico')



@app.route('/buscar', methods=['GET'])
def buscar():
    """
    Endpoint para procesar búsquedas y generar resúmenes.

    Returns:
        JSON con el resumen, tokens utilizados, enlaces y duración
    """
    start_time = datetime.datetime.now()
    pregunta = request.args.get('query')
    if not pregunta:
        return jsonify({"error": "Se requiere el parámetro 'query'"}), 400

    lista_urls = []
    resultado = busqueda(pregunta)
    for i in resultado:
        lista_urls.append(i["link"])

    contenido = extraer_texto(lista_urls)
    sumarizado, input_tokens, output_tokens, cost = sumarizar_gemini(pregunta,contenido)
    
    links_html = "<br>".join([f'<a href="{url}" target="_blank">{url}</a>' for url in lista_urls])
    
    datos_consulta = {
        "pregunta": pregunta,
        "links": lista_urls,
        "contenido": contenido,
        "sumarizado": sumarizado,
        "fecha": datetime.datetime.now(),
        "cost": cost
    }

    insertar_datos_mongodb(datos_consulta)
    end_time = datetime.datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    return jsonify({
        "sumarizado": markdown.markdown(sumarizado),
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "links": links_html,
        "duration": duration
    })



@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    """
    Endpoint para generar un PDF a partir del contenido HTML.

    Returns:
        Archivo PDF generado o mensaje de error
    """
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Se requiere el parámetro 'text'"}), 400
    html = data['text']

    buffer = io.BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=buffer)
    if pisa_status.err:
        return jsonify({"error": "Error al generar el PDF"}), 500
    buffer.seek(0)

    return send_file(
        buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name='output.pdf'
    )

if __name__ == '__main__':
    app.run(
        debug=False,
        host='0.0.0.0',
        port=5000,
        ssl_context=('cert.pem', 'key.pem')
    )
