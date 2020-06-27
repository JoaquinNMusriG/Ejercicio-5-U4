class ManejadorPacientes:
    __pacientes=None

    def __init__(self):
        self.__pacientes=[]

    def agregarPaciente(self, paciente):
        self.__pacientes.append(paciente)

    def getListaPacientes(self):
        return self.__pacientes

    def borrarPaciente(self, paciente):
        self.__pacientes.remove(paciente)

    def actualizarPaciente(self, pacV, pacN):
        for i, paciente in enumerate(self.__pacientes):
            if paciente == pacV:
                self.__pacientes[i] = pacN

    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                pacientes=[paciente.toJSON() for paciente in self.__pacientes]
                )
        return d
