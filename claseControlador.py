from claseVista import nuevoPaciente, mostrarIMC
from claseManejador import ManejadorPacientes

class ControladorPacientes:
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.pacientes = list(repo.obtenerListaPacientes())

    def crearPaciente(self):
        nPaciente = nuevoPaciente(self.vista).show()
        if nPaciente:
            paciente = self.repo.agregarUnPaciente(nPaciente)
            self.pacientes.append(paciente)
            self.vista.agregarPaciente(paciente)

    def seleccionarPaciente(self, index):
        self.seleccion = index
        paciente = self.pacientes[index]
        self.vista.verContactoEnForm(paciente)

    def modificarPaciente(self):
        if self.seleccion==-1:
            return
        pacienteViejo = self.pacientes[self.seleccion]
        pacienteNuevo = self.vista.obtenerCambios()
        paciente = self.repo.modificarPaciente(pacienteViejo, pacienteNuevo)
        self.pacientes[self.seleccion] = paciente
        self.vista.modificarPaciente(paciente, self.seleccion)
        if (not self.vista.verificarPaciente(self.seleccion)):
            self.seleccion=-1

    def borrarPaciente(self):
        if self.seleccion==-1:
            return
        paciente = self.pacientes[self.seleccion]
        self.repo.eliminarPaciente(paciente)
        self.pacientes.remove(paciente)
        self.vista.borrarPaciente(self.seleccion)
        self.seleccion=-1

    def CalcularIMC(self):
        if self.seleccion==-1:
            return
        paciente = self.pacientes[self.seleccion]
        mostrarIMC(self.vista, paciente)
        if (not self.vista.verificarPaciente(self.seleccion)):
            self.seleccion=-1

    def start(self):
        for c in self.pacientes:
            self.vista.agregarPaciente(c)
        self.vista.mainloop()

    def salirGrabarDatos(self):
        self.repo.grabarDatos()
