class Videos:
    def __init__(self,idVideo,nombre,url,fechapublicacion):
        self.__idVideo = idVideo
        self.__nombre = nombre
        self.__url = url
        self.__fechapublicacion = fechapublicacion

    @property
    def idVideo(self):
        return self.__idVideo
    
   
    @property
    def nombre(self):
        return self.__nombre
    
     
    @property
    def url(self):
        return self.__url

    @property
    def fechapublicacion(self):
        return self.__fechapublicacion