'''
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.
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
    

class Cuenta(Persona):
    def __init__(self, titular=None, cantidad=0):
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, nuevo_valor):
        self._titular = nuevo_valor

    @property
    def cantidad(self):
        return self._cantidad
    
    def mostrar(self):
        print(f'Titular: {self._titular.nombre} | Cantidad: {self._cantidad}')

    def ingresar(self, monto):
        if monto > 0:
            self._cantidad += monto

    def retirar(self, monto):
        self._cantidad -= monto

        

if __name__ == '__main__':
    persona1 = Persona()
    persona1.nombre = 'Pepe'
    persona1.edad = 48
    persona1.dni = 20459652

    print('\nCuenta 1')
    cuenta1 = Cuenta()
    cuenta1.titular = persona1
    cuenta1.mostrar()
    cuenta1.ingresar(1500)
    cuenta1.mostrar()
    cuenta1.retirar(500)
    cuenta1.mostrar()

    