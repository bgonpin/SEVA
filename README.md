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

## ⚙️ Funcionalidad Detallada

SEVA permite a los usuarios realizar búsquedas en la web utilizando el motor de búsqueda SearxNG. Los resultados de la búsqueda se analizan para extraer el contenido relevante de las páginas web. Este contenido se utiliza para generar resúmenes concisos utilizando modelos de inteligencia artificial. Los usuarios pueden exportar los resultados de la búsqueda y los resúmenes a archivos PDF. Además, las búsquedas se almacenan en una base de datos MongoDB para su posterior consulta.

### Búsqueda Web

- Los usuarios pueden ingresar palabras clave para realizar búsquedas en la web.
- SEVA utiliza SearxNG para obtener resultados de búsqueda.
- Los resultados se muestran en la interfaz web.

### Extracción de Contenido

- SEVA extrae el contenido principal de las páginas web encontradas en los resultados de búsqueda.
- Se utilizan técnicas de análisis de HTML para identificar el contenido relevante.

### Generación de Resúmenes

- SEVA utiliza modelos de inteligencia artificial para generar resúmenes concisos del contenido extraído.
- Los usuarios pueden ver los resúmenes en la interfaz web.

### Exportación a PDF

- Los usuarios pueden exportar los resultados de la búsqueda y los resúmenes a archivos PDF.
- Los archivos PDF se generan utilizando la librería xhtml2pdf.

### Almacenamiento en MongoDB

- Las búsquedas realizadas por los usuarios se almacenan en una base de datos MongoDB.
- Esto permite a los usuarios consultar sus búsquedas anteriores.

## ⚠️ Posibles Errores y Soluciones

A continuación, se presentan algunos de los posibles errores que pueden ocurrir al utilizar SEVA y sus posibles soluciones:

- **Error de conexión a MongoDB:**
  - Asegúrate de que MongoDB esté instalado y en ejecución.
  - Verifica que la URI de MongoDB en el archivo `.env` sea correcta.
- **Error de conexión a SearxNG:**
  - Asegúrate de que SearxNG esté instalado y en ejecución.
  - Verifica que la URL de SearxNG en el archivo `.env` sea correcta.
- **Error de API de Gemini:**
  - Asegúrate de que la API key de Gemini en el archivo `.env` sea correcta.
  - Verifica que la API de Gemini esté disponible.
- **Error al generar PDF:**
  - Asegúrate de que la librería xhtml2pdf esté instalada correctamente.
  - Verifica que el contenido a exportar sea válido.
- **Errores de red:**
  - Verifica tu conexión a internet.
  - Intenta de nuevo más tarde.

## 🚀 Uso Avanzado

### Configuración de Variables de Entorno

- Las variables de entorno se configuran en el archivo `.env`.
- Asegúrate de que las variables `MONGODB_URI`, `SEARX_URL` y `GEMINI_API_KEY` estén correctamente configuradas.

### Configuración de Certificados SSL

- Los certificados SSL se utilizan para una comunicación segura.
- Puedes generar los certificados SSL utilizando los comandos de `openssl` proporcionados en la sección "Seguridad".

### Personalización de la Interfaz Web

- La interfaz web se puede personalizar modificando los archivos HTML y CSS en el directorio `templates`.

## ❓ Preguntas Frecuentes

- **¿Cómo puedo cambiar el modelo de IA utilizado para la sumarización?**
  - El modelo de IA se configura en el archivo `_sumarizar.py`. Puedes modificar este archivo para utilizar un modelo diferente.
- **¿Cómo puedo añadir un nuevo motor de búsqueda?**
  - Puedes añadir un nuevo motor de búsqueda modificando el archivo `_raspar.py`.
- **¿Cómo puedo contribuir al proyecto?**
  - Consulta el archivo `CONTRIBUTING.md` para obtener más información sobre cómo contribuir al proyecto.
- **¿Dónde puedo encontrar más información sobre las librerías utilizadas?**
  - Consulta la documentación de las librerías utilizadas: Flask, MongoDB, Langchain, Gemini y xhtml2pdf.
