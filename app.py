from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from stt import transcrever_audio
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({'erro': 'Nenhum arquivo enviado'}), 400

    arquivo = request.files['audio']
    filename = secure_filename(arquivo.filename or "audio.webm")
    caminho = os.path.join(UPLOAD_FOLDER, filename)
    arquivo.save(caminho)

    try:
        texto = transcrever_audio(caminho)
        return jsonify({'texto': texto})
    except Exception as e:
        return jsonify({'erro': 'Falha ao transcrever'}), 500
    finally:
        try:
            os.remove(caminho)
        except OSError:
            pass

if __name__ == '__main__':
    app.run(debug=True)