class temas:
    def __init__ (self,idtema,nombre):
        self.__idtema, self.__nombre = idtema, nombre    
   
   @property 
    def idtema(self):
        return self.__idtema
    @property
    def nombre(self):
        return self.__nombre
   
   @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor
   
   @idtema.setter 
    def idtema(self):
        self._idtema


    def AgregarTema(self):
        archivo = open('./archivos/Temas.txt','a',encoding='utf8')
        archivo.write(self.__idtema + '|' + self.__nombre + '\n')
        archivo.close()
    
    @classmethod
    def Agregar(self,ubi,ubi2,contador):
        nombre = input('Nombre: ')
        Lista = []
        archivo1 = open(ubi2, encoding='utf8')
        cont = 6
        for n in archivo1:
            dato = n.split('\n')
            contador = contador - 1
            cont = cont - 1
            Lista.append(dato[0])
            if contador == 0:
                idtema = str(int(dato[0]) + 1)
                Lista.remove(dato[0])
                Lista.append(idtema)
            archivo2 = open(ubi2,"w",encoding = "utf8")
            for a in Lista:
                archivo2.write(a + '\n')
            archivo2.close()
            if cont == 0:
                break
        archivo1.close()
        T = TEMAS(idtema,nombre)
        T.AgregarTema()
