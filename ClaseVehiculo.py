

class Vehiculo:
    __modelo=""
    __puertas=0
    __color=""
    __precioBase=0

    def __init__(self,modelo="",puertas=0,color="",precioBase=0):
        self.__modelo=modelo
        self.__puertas=puertas
        self.__color=color
        self.__precioBase=precioBase 
    def cambiarPrecioBase(self,precio2):
        self.__precioBase=precio2
    def getModelo(self):
        return self.__modelo

    def getPuertas(self):
        return self.__puertas

    def getColor(self):
        return self.__color

    def getPrecioBase(self):
        return self.__precioBase
    def __str__(self):
        return f'Modelo: {self.__modelo},Cantidad de puertas: {self.__puertas},Color: {self.__color},Precio: {self.__precioBase}'  