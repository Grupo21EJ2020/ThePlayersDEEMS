importar  os

clase  Curso_Tema :
    def  _init_ ( self , idCursoTema , idCurso , idTema ):
        auto . idCursoTema  =  idCursoTema
        auto . idCurso  =  idCurso
        auto . idTema  =  idTema
    
    def  agregar_curso_tema ():
        archivo  =  abierto ( "./archivos/cursos_temas.txt" , "a" , codificación = "utf8" )
        
        print ( "Cual es el id del curso" )
        idcursotema  =  input ( ">" )
        print ( "Cual es el id del curso" )
        idcurso  =  input ( ">" )
        print ( "Cual es el id del curso" )
        idtema  =  input ( ">" )

        archivo . escribir ( idcursotema  +  "|"  +  idcurso  +  "|"  +  idtema )
        
        archivo . cerrar ()

    def  consultar_curso_tema ():
        archivo  =  abierto ( "./archivos/cursos_temas.txt" , codificación = "utf8" )

        imprimir ( archivo . leer ())

        archivo . cerrar ()

    def  detalles_curso_tema ():
        archivo  =  abierto ( "./archivos/cursos_temas.txt" , codificación = "utf8" )

        print ( "Cual es el id que necesitas" )
        id_buscar  =  input ( ">" )

        

        archivo . cerrar ()

    def  modificar_cursos_temas ():
        archivo  =  abierto ( "./archivos/cursos_temas.txt" , "r" , codificación = "utf8" )
        archivo_temp  =  abierto ( "./archivos/cursos_temas_temp.txt" , "w" , encoding = "utf8" )

        print ( "Cual es el id que quieres modificar" )
        id_mod  =  input ( ">" )
        print ( "Cual es el nuevo id del tema del curso" )
        idcursotema  =  input ( ">" )
        print ( "Cual es el nuevo id del curso" )
        idcurso  =  input ( ">" )
        print ( "Cual el nuevo id del tema" )
        idtema  =  input ( ">" )

        
        archivo . cerrar ()
        archivo_temp . cerrar ()
        os . eliminar ( "./archivos/cursos_temas.txt" )
        os . renombrar ( "./archivos/cursos_temas_temp.txt" , "./archivos/cursos_temas.txt" )

    def  borrar_curso_tema ():
        archivo  =  abierto ( "./archivos/cursos_temas.txt" , "r" , codificación = "utf8" )
        archivo_temp  =  abierto ( "./archivos/cursos_temas_temp.txt" , "w" , encoding = "utf8" )

        print ( "Id a Borrar" )
        id_borrar  =  input ( ">" )

    
        archivo . cerrar ()
        archivo_temp . cerrar ()
        os . eliminar ( "./archivos/cursos_temas.txt" )
        os . renombrar ( "./archivos/cursos_temas_temp.txt" , "./archivos/cursos_temas.txt" )