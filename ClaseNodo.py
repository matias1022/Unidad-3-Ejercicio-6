from ClaseVehiculo import Vehiculo
from ClaseVehiculoNuevo import VehiculoNuevo

class Nodo:
    __vehiculo=None
    __siguiente=None
    def __init__(self,vehiculo): 
        self.__vehiculo=vehiculo
        self.__siguiente=None

    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente   
        
    def getSig(self):
        return self.__siguiente

    def getVehiculo(self):
        return self.__vehiculo
 
    def getTipo(self):
        return self.__vehiculo
