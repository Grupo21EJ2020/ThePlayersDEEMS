from Empleados import Empleado


    
print("Menu Principal:\n1) Curso\n2) Empleado\n3) Video\n4) Tema\n5) Cuso Tema\n6) Curso Tema Video\n7) Salir") 
opcion=int(input("Elige una opcion: ")) 

if opcion == 1:
      print("Seleccione un Curso\n")
    

elif opcion == 2:
 
 while opcion!=5:    
  print("=====Menu Empleado=====")
  print('1.Agregar\n2.Borrar\n3.Modificar\n4.Consultar todo o Ver detalles\n5.Salir')

  opcion = int(input('Elige una Opcion:'))

  if opcion == 1:
    print ("====Agregar Empleado====\n")
    try:
       archivo = open("Empelados.txt","a")

    except: 
        exit()
        print ("Error")
  
    
    idempleado = input("Ingresar Id:")
    nombre = input("Ingresar Nombre:")
    direccion = input("Ingresar Direccion:")
    print('====Se A Agregado Un Nuevo Registro====')
     
    print(idempleado ,"|" ,nombre ,"|" ,direccion)
  
    archivo.write(idempleado)
    archivo.write("|")
    archivo.write(nombre)
    archivo.write("|" )
    archivo.write(direccion)
    archivo.write("\n")
    
    
    archivo.close()

  elif opcion == 2:
     print("====Eliminacion de Empleados====")
     try:
        archivo = open("Empelados.txt","a")
        
     except: 
        exit()
        print ("Error")
       
     
     archivo.truncate(0)
     print ("Registros Eliminados......")
     archivo.close()
    

  elif opcion == 3:
      print("====Modificar Empleado====\n")    
      def Modificar(archivo, numlinea, texto):
          linea = open(archivo, 'r').readlines()
          linea[numlinea] = texto
          out = open(archivo, 'w')
          out.writelines(linea)
          print("Sea Modificado El Empleado......")
          out.close()
      Modificar('Empelados.txt', 4, '20|Ricardo Daniel Gonzalez Capetillo|Apodaca\n')

  elif opcion == 4:
    print ("Mostrar Empleados\n")
    try:
        archivo = open("Empelados.txt")

    except: 
        exit()
        print ("Error")

    print("\n")
    print(archivo.read())
    print("\n")

    archivo.close()
  elif opcion == 5:
        break
    

  else:
    print("Debes de elegir uns opcion")

elif opcion == 3:
      print("Seleccione un video\n")
    

elif opcion == 4: 
      print("Seleccione un Tema\n")  
    

elif opcion == 5:
      print("Seleccione Curso Tema\n")
    

elif opcion == 6: 
      print("Seleccione Curso Tema Video\n")
    

elif opcion == 7: 
      print("Seleccione Salir\n")  
    


