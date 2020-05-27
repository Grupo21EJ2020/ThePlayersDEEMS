class Temas:
    def_init_(self,idtema,nombre)
    self._idtema = idtema
    self._nombre = nombre

    @property
    def idtema(self):
        return self._idtema

    @property
    def nombre(self):
        return self._nombre
    |
    def ConsultarInfo(self):
        print(f"{'Id Tema' :<10}{'Nombre':<20}")
        print(f"{self.__idTema: <10}{self.__Nombre}")

    def agregarTema(self):
        archivo = open("Temas.txt","a")
        archivo.write(self.__idTema + "|" + self.__Nombre + "\n")
        archivo.close()
