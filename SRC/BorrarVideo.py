def borrar(self):
        f = open("./archivos/videos.txt")
        Lista = []
        for line in f:
            linea = line.split("\n")
            self.__idVideo = linea[0]
                Lista + = line