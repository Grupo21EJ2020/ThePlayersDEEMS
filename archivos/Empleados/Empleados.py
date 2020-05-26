class Empleado:
    def __init__(self,idempleados,nombre,direccion):
        self.__idempleado = idempleados
        self.__nombre = nombre
        self.__direccion = direccion
    
    @property
    def idempleados(self):
        return self.__idempleado
    
   
    
    @property
    def nombre(self):
        return self.__nombre
    
     
    @property
    def direccion(self):
        return self.__direccion

    
    
