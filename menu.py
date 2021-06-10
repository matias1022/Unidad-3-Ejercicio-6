from ClaseObjectEncoder import ObjectEncoder
import os
from ClaseVehiculoNuevo import VehiculoNuevo
from ClaseVehiculoUsado import VehiculoUsado
from ClaseLista import Lista

class Menu:
      __op = 0
      def __init__(self,opcion=0):
        self.__op = opcion
      def Ejecutar(self):
          os.system('cls')
          salir = False
          lista=Lista()
          jsonF=ObjectEncoder()       
          diccionario=jsonF.leerJSONArchivo('vehiculos.json') #se lee el archivo JSON
          lista=jsonF.decodificarDiccionario(diccionario)
          while salir == False:
              print('1-\tInsertar un vehículo en la colección en una posición determinada.')
              print('2-\tAgregar un vehículo a la colección. ')
              print('3-\tDada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.')
              print('4-\tDada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta.')
              print('5-\tMostrar todos los datos, incluido el importe de venta, del vehículo más económico.')
              print('6-\tMostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.')
              print('7-\tAlmacenar los objetos de la colección Lista en el archivo “vehiculos.json”')
              print('0-\tSalir')
            
              self.__op = int(input('Ingrese la opcion: '))
              if self.__op == 1:  
                 x=int(input('Ingresar Posicion:'))
                 NuevoOUsado=input("Ingres si es -Nuevo- o -Usado-:")
                 if NuevoOUsado=="Nuevo" or NuevoOUsado=="Usado":
                    modelo=input("Ingresar Modelo:")
                    puertas=int(input("Ingresar Cantidad Puertas:"))
                    color=input("Ingresar Color:")
                    precio=float(input("Ingresar precio:"))
                    if  NuevoOUsado=="Nuevo":
                        version=input("Ingrese la Version(full o base):")
                        if version=="full" or version=="base":
                            unVehiculo=VehiculoNuevo(modelo,puertas,color,precio,version)

                        else: print("Se ha ingresado una version Invalida:")
                    else:
                       marca=input("\nIngresar marca: ")
                       patente=input("\nIngresar patente: ")
                       anio=int(input("\nIngresar  año: "))
                       Km=int(input("\nIngrese los kilometros recorridos: "))
                       unVehiculo=VehiculoUsado(modelo,puertas,color,precio,marca,patente,anio,Km)
                 else: 
                    print("Se ha ingresado incorrectamente si era nuevo o usado")      
                 print(unVehiculo) 
                # lista.agregarVehiculo(unVehiculo)      
                 lista.insertarVehiculo(x,unVehiculo)
        
                
              elif self.__op == 2: 

                 NuevoOUsado=input("Ingres si es -Nuevo- o -Usado-:")
                 if NuevoOUsado=="Nuevo" or NuevoOUsado=="Usado":
                    modelo=input("Ingresar Modelo:")
                    puertas=int(input("Ingresar Cantidad Puertas:"))
                    color=input("Ingresar Color:")
                    precio=float(input("Ingresar precio:"))
                    if  NuevoOUsado=="Nuevo":
                        version=input("Ingrese la Version(full o base):")
                        if version=="full" or version=="base":
                            unVehiculo=VehiculoNuevo(modelo,puertas,color,precio,version)
                        else: print("Se ha ingresado una version Invalida:")
                    else:
                       marca=input("\nIngresar marca: ")
                       patente=input("\nIngresar patente: ")
                       anio=int(input("\nIngresar  año: "))
                       Km=int(input("\nIngrese los kilometros recorridos: "))
                       unVehiculo=VehiculoUsado(modelo,puertas,color,precio,marca,patente,anio,Km)
                 else: 
                    print("Se ha ingresado incorrectamente si era nuevo o usado")    
                 lista.agregarVehiculo(unVehiculo)

              elif self.__op == 3: 
                  x=int(input("Ingresar posicion"))
                  lista.mostrarVehiculo(x)
                  
                  
              elif self.__op == 4: 
                   patente=input("Ingresar patente del vehiculo: ")
                   lista.modificar(patente)
              elif self.__op == 5: 
                    print("Buscar auto mas economico")
                    lista.minimo()
              elif self.__op == 6: 
                    print("---------VEHICULOS---------")
                    lista.mostrarTodo()
              elif self.__op == 7: 
                          
                    d=lista.toJSON()
                    jsonF.guardarJSONArchivo(d,'vehiculos.json')
                    print("Se ha guardado correctamente")
               
               


              elif self.__op == 0: #Salir
                  salir = True
              else:
                 print('Opcion ingresada incorrecta')
                 input('Presiona ENTER para continuar...')


          print('Cerrando Menú..')   