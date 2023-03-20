'''
REQUERIMIENTOS:
Se identifica la necesidad de digitalizar y automatizar las inscripciones a codo a codo.
Se debe poder gestionar los cursos, inscripciones y comisiones que lleva adelante el programa.

Quienes tengan interes en poder cursar el programa deberan realizar la inscripcion de manera online,
completando un formulario con los datos personales basicos y seleccionando un curso disponible
dependiendo de la categoría en la que estén interesados (programación, testing, diseño).

Además, una persona con el rol necesario para realizar las gestiones de las distintas categorías, cursos y clases
con el fin de qué estén disponibles para quiénes ya se consideran estudiantes del programa (han sido inscriptos de manera online).

Quien poseea este rol también podrá gestionar los proyectos que se desarrollen durante la cursada para que puedan estar visibles al público general.
Se observa que quienes posean este rol tendrán información en el sistema que incluya su teléfono, domicilio y una foto de perfil.  
'''

from abc import ABCMeta

class Curso():
    OPCIONES_CATEGORIAS = {'PROGRAMACIÓN', 'TESTING', 'DISEÑO'}

    def __init__(self, curso, comision, categoria):
        self.curso = curso
        self.comision = comision
        self.categoria = categoria
        self._proyectos = set()

    def __str__(self):
        return f'{self.curso} (#{self.comision}) - {self.categoria} - Proyectos: {self.proyectos}'

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        if categoria.upper() in Curso.OPCIONES_CATEGORIAS:
            self._categoria = categoria.upper()
        else:
            raise ValueError(f'La categoría "{categoria}" no existe entre las opciones disponibles')
    
    @property
    def proyectos(self):
        return [proyecto.proyecto for proyecto in self._proyectos]
    
    def agregar_proyecto(self, proyecto):
        self._proyectos.add(proyecto)

    def quitar_proyecto(self, proyecto):
        self._proyectos.remove(proyecto)


class Proyecto():
    def __init__(self, proyecto, visible=False):
        self.proyecto = proyecto
        self._visible = visible

    def __str__(self):
        return self.proyecto 

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, visible):
        if isinstance(visible, bool):
            self._visible = visible
        else:
            raise ValueError('Solo se permite un valor booleano')


class Usuario(metaclass=ABCMeta):
    def __init__(self, nombre, apellido, dni, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Alumno(Usuario):
    def __init__(self, nombre, apellido, dni, email, curso=None):
        super().__init__(nombre, apellido, dni, email)
        self.curso = curso

    def __str__(self):
        return f'{self.nombre} {self.apellido} - Curso: {self.curso.curso} #{self.curso.comision}'


class Coordinador(Usuario):
    def __init__(self, nombre, apellido, dni, email, telefono, domicilio, avatar):
        super().__init__(nombre, apellido, dni, email)
        self.telefono = telefono
        self.domicilio = domicilio
        self.avatar = avatar



if __name__ == '__main__':
    # Crear coordinador
    coordinador1 = Coordinador('Maximiliano', 'Torres', '33999999', 'mtorres@mail.com', '+54 9 11 1234 1234', 'Siempreviva 123', '/img/foto_maxi.jpg')
    print(f'\nCoordinador: {coordinador1}')
    
    # Crear cursos
    python = Curso('Python', 10500, 'Programación')
    java = Curso('Java', 10501, 'Programación' )
    diseño_web = Curso('Diseño gráfico', 20500, 'Diseño')
    print(f'\nCurso 1: {python}')
    print(f'Curso 2: {java}')
    print(f'Curso 3: {diseño_web}')

    # Crear proyectos
    calculadora = Proyecto('Calculadora', True)
    sistema_de_gestion = Proyecto('Sistema de gestión', False)
    aplicacion_web = Proyecto('Aplicación Web', False)
    print(f'\nProyecto 1: {calculadora}')
    print(f'Proyecto 2: {sistema_de_gestion}')
    print(f'Proyecto 3: {aplicacion_web}')

    # Asignarlos a cursos
    java.agregar_proyecto(calculadora)
    diseño_web.agregar_proyecto(aplicacion_web)
    python.agregar_proyecto(calculadora)
    python.agregar_proyecto(sistema_de_gestion)
    python.agregar_proyecto(aplicacion_web)
    python.quitar_proyecto(aplicacion_web)
    print(f'\nCurso 1: {python}')
    print(f'Curso 2: {java}')
    print(f'Curso 3: {diseño_web}')

    # Crear alumnos
    alumno1 = Alumno('Juan', 'Pérez', '30999999', 'jperez@mail.com', python)
    alumno2 = Alumno('Carla', 'Gómez', '31999999', 'cgomez@mail.com', java)
    alumno3 = Alumno('Roberto', 'García', '32999999', 'rgarcia@mail.com', diseño_web)
    print(f'\nAlumno 1: {alumno1}')
    print(f'Alumno 2: {alumno2}')
    print(f'Alumno 3: {alumno3}\n')

    # Testear errores
    #unity = Curso('Python', 10500, 'videojuegos')
    #python.categoria = 'framework web'


