from claseRepositorio import Respositorio
from claseVista import Aplicacion
from claseControlador import ControladorPacientes
from claseObjectEncoder import ObjectEncoder

if __name__ == "__main__":
    jsonF = ObjectEncoder('contactos.json')
    repositorio = Respositorio(jsonF)
    vista = Aplicacion()
    controlador = ControladorPacientes(repositorio, vista)
    vista.setControlador(controlador)
    controlador.start()
    controlador.salirGrabarDatos()
