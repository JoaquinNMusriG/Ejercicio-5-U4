import re

class Paciente:
    prueba = re.compile("[a-zA-Z]")
    __Nombre = None
    __Apellido = None
    __Telefono = None
    __Altura = None
    __Peso = None

    def __init__(self, nombre, apellido, telefono, altura, peso):
        if nombre.isalpha():
            self.__Nombre = nombre
        else:
            raise ValueError('Nombre inválido')
        #self.__Nombre = self.requerido(nombre, re.compile(r"[a-zA-Z]{1,30}"), 'Nombre inválido')     #No sirve deja poner numeros
        if apellido.isalpha():
            self.__Apellido = apellido
        else:
            raise ValueError('Apellido inválido')
        #self.__Apellido = self.requerido(apellido, re.compile(r"[a-zA-Z]{1,30}"), 'Apellido inválido')
        self.__Telefono = self.requerido(telefono, re.compile(r"\([0-9]{3}\)[0-9]{7}"), 'Teléfono inválido')
        try:
            self.__Altura = int(altura)
        except ValueError:
            raise ValueError('Altura inválida')
        #self.__Altura = self.requerido(altura, re.compile(r"[0-9]{1,4}"), 'Altura inválida')   #No sirve deja poner letras
        try:
            self.__Peso = float(peso)
        except ValueError:
            raise ValueError('Peso inválido')
        #self.__Peso = self.requerido(peso, re.compile(r"[\.0-9]{1,4}"), 'Peso inválido')

    def getApellido(self):
        return self.__Apellido

    def getNombre(self):
        return self.__Nombre

    def getTelefono(self):
        return self.__Telefono

    def getAltura(self):
        return self.__Altura

    def getPeso(self):
        return self.__Peso

    def requerido(self, valor, regex, mensaje):
        if (not valor) or (not regex.match(valor)):
            raise ValueError(mensaje)
        return valor

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                        nombre = self.__Nombre,
                        apellido = self.__Apellido,
                        telefono = self.__Telefono,
                        altura = self.__Altura,
                        peso = self.__Peso
                    )
            )
        return d
