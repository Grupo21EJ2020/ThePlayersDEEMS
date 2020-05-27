# Modifica videos

def Modificar(archivo, numlinea, texto):
          linea = open(archivo, 'r').readlines()
          linea[numlinea] = texto
          out = open(archivo, 'w')
          out.writelines(linea)
          print("Modificar video")
          out.close()
      Modificar('videos.txt', 1|Curso Python para Principiantes|https://www.youtube.com/watch?v=chPhlsHoEPo|22/01/2019\n')


      archivo.close()