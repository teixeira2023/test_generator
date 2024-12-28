import os
from flask import Blueprint, render_template, request, redirect, url_for
from core.file_processor import process_file

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename.endswith('.txt'):
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            frases_filtradas, estatisticas = process_file(file_path)
            return render_template('index.html', frases=frases_filtradas, stats=estatisticas)
        else:
            return "Por favor, envie um arquivo .txt válido.", 400
    
    return render_template('index.html')
