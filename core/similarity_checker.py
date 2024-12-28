from difflib import SequenceMatcher

def calcular_similaridade(frase1, frase2):
    return SequenceMatcher(None, frase1, frase2).ratio()

def remover_frases_similares(lista_frases, limiar=0.9):
    frases_unicas = []
    for frase in lista_frases:
        if not any(calcular_similaridade(frase, f) > limiar for f in frases_unicas):
            frases_unicas.append(frase)
    return frases_unicas
