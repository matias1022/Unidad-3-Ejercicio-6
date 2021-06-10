
from ClaseLista import Lista
from ClaseVehiculoNuevo import VehiculoNuevo
from ClaseVehiculoUsado import VehiculoUsado
from menu import Menu

def test():
    unVehiculoNuevo=VehiculoNuevo('Mercedes',5,'negro',5950000.0,'base')
    print(unVehiculoNuevo)
    print(unVehiculoNuevo.calculoImporteVenta())
    lista=Lista()
    lista.agregarVehiculo(unVehiculoNuevo)

if __name__ == '__main__':
    test()
    input()
    menu=Menu()
    menu.Ejecutar()