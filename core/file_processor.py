import os
from .similarity_checker import remover_frases_similares

def process_file(file_path):
    with open(file_path, 'r') as file:
        frases = [linha.strip() for linha in file.readlines()]
    
    frases_filtradas = remover_frases_similares(frases)
    
    estatisticas = {
        'total': len(frases),
        'removidas': len(frases) - len(frases_filtradas),
        'finais': len(frases_filtradas)
    }
    
    return frases_filtradas, estatisticas
