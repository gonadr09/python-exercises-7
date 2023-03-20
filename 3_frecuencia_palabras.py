'''
3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
'''

import re

def frecuencia_de_palabras(texto):
    texto_sin_signos = re.sub('[,.;:¿?¡!\'\"]', "", texto)
    palabras = texto_sin_signos.split()
    palabras_en_min = [palabra.lower() for palabra in palabras]
    palabras_no_repetidas = set(palabras_en_min)
    diccionario = {} 
    for palabra in palabras_no_repetidas:
        diccionario[palabra] = palabras_en_min.count(palabra)    
    return diccionario


if __name__ == '__main__':
    print('\n3. Frecuencia de palabras en diccionario')
    texto = '¡Hola, amigo! ¿cómo estás, amigo? esto es una prueba que cuenta palabras repetidas, es solo eso, una prueba, mi amigo.'
    print(f'Texto original: {texto}')
    print(f'Diccionario: {frecuencia_de_palabras(texto)}')