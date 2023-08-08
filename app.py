from flask import Flask, request, render_template, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'image' not in request.files:
        return "No se ha seleccionado ninguna imagen", 400

    image = request.files['image'].read()

    # Remueve el fondo de la imagen
    image_without_background = remove(image)

    # Crea un objeto io.BytesIO y guarda los datos de la imagen sin fondo
    image_stream = io.BytesIO(image_without_background)

    # Retorna la imagen sin fondo como archivo descargable
    return send_file(image_stream, mimetype='image/png', download_name='imagen_sin_fondo.png')

if __name__ == '__main__':
    app.run(debug=True)
