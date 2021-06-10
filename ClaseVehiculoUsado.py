from ClaseVehiculo import Vehiculo
from datetime import date

class VehiculoUsado(Vehiculo):
    __marca=''
    __patente=''
    __anio=0
    __Km=0


    def __init__(self, modelo, puertas, color, precioBase,marca,patente,anio,Km):
        super().__init__(modelo, puertas, color, precioBase)
        self.__marca=marca
        self.__patente=patente
        self.__anio=anio
        self.__Km=Km
    def getModelo(self):
        return super().getModelo()
    def getPatente(self):
        return self.__patente
    def getAnio(self):
        return self.__anio
    def getKm(self):
        return self.__Km 
    def getMarca(self):
        return self.__marca
    def calculoImporteVenta(self):
        anio=int(date.today().year)   
        anios=anio-self.__anio
        importe=int(super().getPrecioBase()) - ((1/100)*anios*int(super().getPrecioBase()))
        if self.__Km>100000:
            importe=int(super().getPrecioBase()) - ((2/100)*anios*int(super().getPrecioBase()))
        return importe  

    def toJSON(self):
        d=dict(
         __class__=self.__class__.__name__,
         __atributos__=dict(
                modelo=self.getModelo(),
                puertas=self.getPuertas(),
                color=self.getColor(),
                precioBase=self.getPrecioBase(),
                marca=self.__marca,
                patente=self.__patente,
                anio=self.__anio,
                Km=self.__Km
               )
        )
        return d