from sys import version
from zope.interface import Interface
from zope.interface import implementer
from ClaseVehiculo import Vehiculo
from ClaseNodo import Nodo
from ClaseInterfaz import interface
from ClaseVehiculoUsado import VehiculoUsado
from ClaseVehiculoNuevo import VehiculoNuevo
@implementer(interface)

class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0
    
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def agregarVehiculo(self,vehiculo):
            isinstance(vehiculo,Vehiculo)
            nodo=Nodo(vehiculo)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo=nodo
            self.__actual=nodo
            self.__tope= self.__tope+1
            print("El Vehiculo fue agregado")
   
    def insertarVehiculo(self,x,unVehiculo):

        aux=self.__comienzo
        encontro=False
        i=0
        ant=aux
        if 0<x<=self.__tope+1:
            if i==x-1:
                if self.__comienzo==None:
                    self.agregarVehiculo(unVehiculo)
                else:
                    nodo=Nodo(unVehiculo)
                    nodo.setSiguiente(aux)
                    aux.setSiguiente(aux.getSig())
                    self.__comienzo=nodo
                    self.__actual=nodo
                    self.__tope+=1
                    print("El Vehiculo fue agregado")
            else:
                ant=aux
                while aux!=None and encontro==False:
                    if i==x-1:
                        encontro=True
                    else:
                        i+=1
                        ant=aux
                        aux=aux.getSig()

                if i==x-1:
                    nodo=Nodo(unVehiculo)
                    ant.setSiguiente(nodo)
                    nodo.setSiguiente(aux)
                    self.__tope+=1
                    print("El tope es:")
                    print(self.__tope)
        else: print("Posicion Incorrecta")

    def mostrarVehiculo(self,x):
        aux=self.__comienzo
        encontro=False
        i=0
        ant=aux
        if 0<x<=self.__tope:
            if i==x-1:
                if self.__comienzo==None:
                    print('--ERROR--')
                    print("No hay Vehiculos")
                else:
                    print(f'Aqui en la posicion: {x} se encuentra:')
                    if type(aux.getTipo()==VehiculoNuevo):
                        print("Vehiculo Nuevo")
                    else: print("Vehiculo Usado") 

            else:
                ant=aux
                while aux!=None and encontro==False:
                    if i==x-1:
                        encontro=True
                    else:
                        i+=1
                        ant=aux
                        aux=aux.getSig()

                if i==x-1:
                    print(f'Aqui en la posicion:{x}  se encuentra: ')
                    if type(aux.getTipo()==VehiculoNuevo):
                        print("Vehiculo Nuevo")
                    else: print("Vehiculo Usado")
        else:
            print ("Se ha ingresado una mala posicion")   
    def modificar(self,paten):
          i=0
          aux=self.__comienzo
          while i< self.__tope and aux !=None and paten!= aux.getTipo().getPatente():
                aux=aux.getSig()
                i+=1
          if i<self.__tope:
                precio2=float(input("\nIngrese el nuevo precio: "))
                aux.getTipo().cambiarPrecioBase(precio2)
                print(f"Nuevo precio base: {aux.getTipo().getPrecioBase()}")
                print(f"Precio Venta: {aux.getTipo().calculoImporteVenta()}")
    def minimo(self):
         i=0
         aux=self.__comienzo
         min=9999999   
         while i< self.__tope and aux!=None:
                if float(aux.getTipo().calculoImporteVenta())<min:
                    min=float(aux.getTipo().calculoImporteVenta())
                else:aux=aux.getSig()
                i+=1
         print(f"El vehiculo mas economico es:{aux.getTipo()}")
         if isinstance(aux.getTipo(),VehiculoNuevo):
             print(f"Modelo:{aux.getTipo().getModelo()},Venta:{aux.getTipo().calculoImporteVenta()}")
         if isinstance(aux.getTipo(),VehiculoUsado):
             print(f"Modelo:{aux.getTipo().getModelo()},Patente: {aux.getTipo().getPatente},Año: {aux.getTipo().getAnio()},Km:{aux.getKm}")         
    
    def mostrarTodo(self):
        aux = self.__comienzo
        while aux!=None:
            print("\n------Auto-------")
            print (f"Modelo: {aux.getTipo().getModelo()}Cantidad Puertas: {aux.getTipo().getPuertas()}Importe:{aux.getTipo().calculoImporteVenta()}")
            aux = aux.getSig()
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            vehiculo=self.__actual.getTipo()
            self.__actual=self.__actual.getSig()
            return vehiculo



    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            vehiculos=[vehiculo.toJSON() for vehiculo in self]
        )
        return d     