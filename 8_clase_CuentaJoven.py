'''
8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta.
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


class CuentaJoven(Cuenta):
    def __init__(self, titular=None, cantidad=0, bonificacion=None):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, nuevo_valor):
        self._bonificacion = nuevo_valor

    def mostrar(self):
        print(f'Titular: {self._titular.nombre} (Cuenta Joven) | Cantidad: {self._cantidad} | Bonificación: {self._bonificacion}')

    def es_titular_valido(self):
        return self._titular.edad >= 18 and self._titular.edad < 25
    
    def retirar(self, monto):
        if self.es_titular_valido():
            self._cantidad -= monto



if __name__ == '__main__':
    persona1 = Persona('Carla', 15, 40123546)
    print('\nPersona 1')
    persona1.mostrar()

    print('\nCuenta 1')
    cuenta_joven1 = CuentaJoven(persona1, 0, '10%')
    cuenta_joven1.mostrar()
    cuenta_joven1.ingresar(1500)
    cuenta_joven1.mostrar()
    cuenta_joven1.retirar(500)
    cuenta_joven1.mostrar()

    persona2 = Persona('Lucas', 20, 38546123)
    print('\nPersona 2')
    persona2.mostrar()

    print('\nCuenta 2')
    cuenta_joven2 = CuentaJoven(persona2, 0, '10%')
    cuenta_joven2.mostrar()
    cuenta_joven2.ingresar(1500)
    cuenta_joven2.mostrar()
    cuenta_joven2.retirar(500)
    cuenta_joven2.mostrar()