import tkinter as tk
from tkinter import messagebox
from clasePaciente import Paciente

class ListaBoxPacientes(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.listab = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.listab.yview)
        self.listab.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.listab.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, paciente, index=tk.END):
        text = "{}, {}".format(paciente.getNombre(), paciente.getApellido())
        self.listab.insert(index, text)

    def borrar(self, index):
        self.listab.delete(index) 

    def modificar(self, paciente, index):
        self.borrar(index)
        self.insertar(paciente, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.listab.curselection()[0])
        self.listab.bind("<Double-Button-1>", handler)

class FormularioPacientes(tk.LabelFrame):
    fields = ( "Nombre", "Apellido", "Teléfono", 'Altura', 'Peso')
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Paciente", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def mostrarEstadoPacienteEnFormulario(self, paciente):
        values = (paciente.getNombre(), paciente.getApellido(), paciente.getTelefono(), paciente.getAltura(), paciente.getPeso())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def crearPacienteDesdeFormulario(self):
        values = [e.get() for e in self.entries]
        paciente=None
        try:
            paciente = Paciente(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return paciente

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

class nuevoPaciente(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.unPaciente = None
        self.form = FormularioPacientes(self)
        self.btn_confirmar = tk.Button(self, text="Confirmar", command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_confirmar.pack(pady=10)

    def confirmar(self):
        self.unPaciente = self.form.crearPacienteDesdeFormulario()
        if self.unPaciente:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.unPaciente

class mostrarIMC(tk.Toplevel):
    def __init__(self, parent, paciente):
        super().__init__(parent)
        self.title('IMC')
        self.IMCLbl = tk.Label(self, text="IMC")
        self.CompCorpLbl = tk.Label(self, text="Composicion Corporal")
        self.btn_volver = tk.Button(self, text='Volver',command=self.destroy)
        self.IMCEnt = tk.Entry(self, width=25)
        self.CCEnt = tk.Entry(self, width=25)
        self.IMCLbl.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.IMCEnt.grid(row = 0, column = 1, padx = 10, pady = 10)
        self.CompCorpLbl.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.CCEnt.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.btn_volver.grid(row = 3, column = 0, padx = 10, pady = 10)

        altura = int(paciente.getAltura())
        peso = float(paciente.getPeso())
        mtr = (altura / 100) * (altura / 100)
        imc = peso / mtr
        self.IMCEnt.insert(0,'{:0.6f}'.format(imc))
        if imc < 18.5:
            self.CCEnt.insert(0,'Peso inferior al normal')
        elif imc < 24.9:
            self.CCEnt.insert(0,'Normal')
        elif imc < 29.9:
            self.CCEnt.insert(0,'Peso superior al normal')
        else:
            self.CCEnt.insert(0,'Obesidad')

        self.grab_set()
        self.wait_window()

class BotonesFormularioPaciente(FormularioPacientes):
    def __init__(self, master):
        super().__init__(master)
        self.btn_save = tk.Button(self, text="Guardar")
        self.btn_delete = tk.Button(self, text="Borrar")
        self.btn_IMC = tk.Button(self, text="Ver IMC")
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_IMC.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)

    def bind_save(self, callback):
        self.btn_save.config(command=callback)

    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)

    def bind_IMC(self, callback):
        self.btn_IMC.config(command=callback)

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Pacientes")
        self.listB = ListaBoxPacientes(self, height=15)
        self.form = BotonesFormularioPaciente(self)
        self.btn_new = tk.Button(self, text="Agregar Contacto")
        self.listB.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self, ctrl):
        self.btn_new.config(command=ctrl.crearPaciente)
        self.listB.bind_doble_click(ctrl.seleccionarPaciente)
        self.form.bind_save(ctrl.modificarPaciente)
        self.form.bind_delete(ctrl.borrarPaciente)
        self.form.bind_IMC(ctrl.CalcularIMC)

    def agregarPaciente(self, paciente):
        self.listB.insertar(paciente)

    def modificarPaciente(self, paciente, index):
        self.listB.modificar(paciente, index)

    def borrarPaciente(self, index):
        self.form.limpiar()
        self.listB.borrar(index)

    def obtenerCambios(self):
        return self.form.crearPacienteDesdeFormulario()

    def verContactoEnForm(self, paciente):
        self.form.mostrarEstadoPacienteEnFormulario(paciente)
