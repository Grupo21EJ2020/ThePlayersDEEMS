class Cursos:
    def_init(self,idcurso,descripcion,empleado)
        self._idcurso = idcurso
        self._descripcion = descripcion
        self._empleado = empleado
    
    @property
    def idcurso(self):
        return self._idcurso
    
    @property
    def descripcion (self):
        return self._descripcion

    @property
    def empleado(self):
        return self._empleado
