import json
from ClaseLista import Lista
from ClaseVehiculoNuevo import VehiculoNuevo
from ClaseVehiculoUsado import VehiculoUsado
from pathlib import Path
from ClaseVehiculo import Vehiculo


class ObjectEncoder(object):

    def guardarJSONArchivo(self, vehiculos, archivo):   
        with open(archivo, "w", encoding="UTF-8")as destino:
            json.dump(vehiculos, destino, indent=4)
        destino.close()
        print("\nGuardado con exito!")

    def leerJSONArchivo(self, archivo):
        with open(archivo, encoding="UTF-8")as fuente:
            d=json.load(fuente)
            fuente.close()
            return d

    def decodificarDiccionario(self, d):
        if '__class__'not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Lista':
                vehiculos=d['vehiculos']
                dVehiculo=vehiculos[0]
                lista=class_()
                for i in range(len(vehiculos)):
                    dVehiculo=vehiculos[i]
                    class_name=dVehiculo.pop('__class__')
                    class_=eval(class_name)
                    print(class_name)
                    atributos=dVehiculo['__atributos__']
                    unVehiculo=class_(**atributos)
                    lista.agregarVehiculo(unVehiculo)
            return lista
    