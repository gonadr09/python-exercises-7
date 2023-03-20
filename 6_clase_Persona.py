'''
6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construya los siguientes métodos para la clase:
- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
- mostrar(): Muestra los datos de la persona.
- Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
'''

class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_valor):
        self._nombre = nuevo_valor

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            self._edad = nuevo_valor
        else:
            raise TypeError('Ingrese un número entero para la edad')

    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, nuevo_valor):
        if isinstance(nuevo_valor, int):
            self._dni = nuevo_valor
        else:
            raise TypeError('Ingrese un número entero para el DNI')
        
    def mostrar(self):
        print(f'Nombre: {self._nombre} | Edad: {self._edad} | DNI: {self._dni}')

    def es_mayor_de_edad(self):
        return self._edad >= 18
    

if __name__ == '__main__':
    persona1 = Persona()
    persona1.nombre = 'Pepe'
    persona1.edad = 48
    persona1.dni = 20459652
    print('\nPersona 1')
    persona1.mostrar()
    print(f'¿Es mayor de edad? {persona1.es_mayor_de_edad()}')
    #persona1.edad = '18'  # test validación
    #persona1.dni = '30546894'  # test validación

    print('\nPersona 2')
    persona2 = Persona('Carla', 15, 40123546)
    persona2.mostrar()
    print(f'¿Es mayor de edad? {persona2.es_mayor_de_edad()}')
    