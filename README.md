# SEVA - Sumarizador y Extractor de Contenido Web con IA

SEVA es una aplicación web desarrollada en Python que permite realizar búsquedas en la web, extraer contenido relevante y generar resúmenes utilizando inteligencia artificial.

## 🚀 Características

- Búsqueda web utilizando SearxSearch
- Extracción de contenido de páginas web
- Generación de resúmenes utilizando modelos de IA
- Exportación de resultados a PDF
- Almacenamiento de búsquedas en MongoDB
- Interfaz web intuitiva

## 🛠️ Tecnologías Utilizadas

- Python 3
- Flask - Framework web
- MongoDB - Base de datos
- Langchain - Utilidades de búsqueda
- Gemini - Modelo de IA para sumarización
- xhtml2pdf - Generación de PDFs

## 📋 Requisitos Previos

- Python 3.8 o superior
- MongoDB
- Instancia de SearxNG
- Credenciales de API para Gemini

## ⚙️ Configuración

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/SEVA.git
cd SEVA
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura las variables de entorno en un archivo `.env`:
```
MONGODB_URI=tu_uri_de_mongodb
SEARX_URL=tu_url_de_searx
GEMINI_API_KEY=your_api_key_here
```

## 🚀 Ejecución

Para ejecutar la aplicación:

```bash
python index.py
```

La aplicación estará disponible en `https://localhost:5000`

## 🔒 Seguridad

La aplicación utiliza HTTPS con certificados SSL para una comunicación segura.

Para generar los certificados SSL necesarios (`key.pem` y `cert.pem`), puedes usar los siguientes comandos de `openssl`:

```bash
openssl genrsa -out key.pem 2048
openssl req -new -x509 -key key.pem -out cert.pem -days 365
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, lee [CONTRIBUTING.md](CONTRIBUTING.md) para detalles sobre nuestro código de conducta y el proceso para enviarnos pull requests.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- [SearxNG](https://searx.github.io/searxng/) por proporcionar el motor de búsqueda
- La comunidad de código abierto por las herramientas y librerías utilizadas
