'''
4. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.
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

def palabra_mas_repetida(diccionario):
    lista_de_llaves = list(diccionario.keys())
    resultado = (lista_de_llaves[0], diccionario[lista_de_llaves[0]])
    for palabra in lista_de_llaves:
        if diccionario[palabra] > resultado[1]:
            resultado = (palabra, diccionario[palabra])
    return resultado
        

if __name__ == '__main__':
    texto = '¡Hola, amigo! ¿cómo estás, amigo? esto es una prueba que cuenta palabras repetidas, es solo eso, una prueba, mi amigo.'
    diccionario = frecuencia_de_palabras(texto)

    print('\n4. Palabra más repetida')
    print(f'Texto original: {texto}')
    print(f'Palabra más repetida: {palabra_mas_repetida(diccionario)}')