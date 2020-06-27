from claseManejador import ManejadorPacientes

class Respositorio:
    __jsonF=None
    __manejador=None

    def __init__(self, jsonF):
        self.__jsonF = jsonF
        try:
            diccionario = self.__jsonF.leerJSONArchivo()
            self.__manejador = self.__jsonF.decodificarDiccionario(diccionario)
        except FileNotFoundError:
            self.__manejador = ManejadorPacientes()

    def obtenerListaPacientes(self):
        return self.__manejador.getListaPacientes()

    def agregarUnPaciente(self, paciente):
        self.__manejador.agregarPaciente(paciente)
        return paciente

    def modificarPaciente(self, pacienteV, pacienteN):              
        self.__manejador.actualizarPaciente(pacienteV, pacienteN)
        return pacienteN

    def eliminarPaciente(self, paciente):
        self.__manejador.borrarPaciente(paciente)

    def grabarDatos(self):
        self.__jsonF.guardarJSONArchivo(self.__manejador.toJSON())
