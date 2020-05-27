consultar

archivo = open("./archivos/videos.txt", "r", encoding = "utf8")

for x in archivo:

       videos = x.split('|')
       print("numero",videos [0])
       print("nombre",videos [1])
       print("enlace",videos [2])
       print("fechapublicacion",videos [3])

archivo.cose()