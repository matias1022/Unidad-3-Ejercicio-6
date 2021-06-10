from ClaseVehiculo import Vehiculo

class ManejaVehiculo():
    __vehiculos=[]

    def __init__(self):
        self.__vehiculos=[]

    def agregaVehiculo(self,unVehiculo):
        if isinstance(unVehiculo,Vehiculo):
            self.__vehiculos.append(unVehiculo)

    def __str__(self):
        s=''
        for unVehiculo in self.__vehiculos:
            s+=unVehiculo.__str__()+'\n'
        return s