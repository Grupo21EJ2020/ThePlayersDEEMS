class cursos:
    def_init(self,idcurso,descripcion,empleado)
         self._idcurso = idcurso
         self._descripcion = descripcion
         self._eempleado = empleado

    @property
    def idcurso(self)
        return self._idcurso

    @property
    def descripcion(self)
        return self._descripcion

    @property
    def empleado(self)
        return self._empleado
    def Agregar(self):
        archivo = open("./archivos/curso.txt","a",encoding='utf8')
        archivo.write( str(self.__idcurso) + '|' + self.__descripcion + '|' + str(self.__idempleado))
        archivo.write("\n")    
        archivo.close()
    def Eliminar(self):
        f = open("./archivos/curso.txt")
        Lista = []
        for line in f:
            linea = line.split("\n")
            self.__idcurso = linea[0]
            self.__descripcion = linea[1]
            self.__idempleado = linea[2]
            if self.__idcurso != self.__idcurso:
                Lista += line
