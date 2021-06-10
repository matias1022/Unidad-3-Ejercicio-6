from ClaseVehiculo import Vehiculo


class VehiculoNuevo(Vehiculo):
    __version=""
    marca="Mercedes"

    def __init__(self,modelo="",puertas=0,color="",precioBase=0,version=""):
        super().__init__(modelo,puertas,color,precioBase)
        self.__version=version
    @classmethod
    def getMarca(cls):
        return cls.__marca
    
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__ = dict(
                             modelo=self.getModelo(),
                             puertas=self.getPuertas(),
                             color=self.getColor(),
                             precioBase=self.getPrecioBase(),
                             version=self.__version
                             )
           )
        return d
    def calculoImporteVenta(self): 
        precioVenta=self.getPrecioBase()+10*self.getPrecioBase()/100
        if self.__version == 'full':
            precioVenta+=2*self.getPrecioBase()/100
        return precioVenta       
    def __str__(self):
        s=""
        s=super().__str__()
        s+=f"Version:{self.__version}"
        return s