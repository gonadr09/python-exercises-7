'''
5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.
'''

def get_int_iterativa():
    entero = None
    while True:
        respuesta = input('Ingrese un número entero: ')
        try:
            entero = int(respuesta)
            break
        except ValueError as e:
            print('El valor ingresado no es un número')
    return entero


def get_int_recursiva(entero=None):
    respuesta = input('Ingrese un número entero: ')
    try:
        entero = int(respuesta)
    except ValueError as e:
        print('El valor ingresado no es un número')
        entero = get_int_recursiva()
    finally:
        return entero


if __name__ == '__main__':
    print('\n5. INT a STR')
    print('\na. Resolución con función iterativa:')
    print(get_int_iterativa())
    print('\nb. Resolución con función recursiva:')
    print(get_int_recursiva())