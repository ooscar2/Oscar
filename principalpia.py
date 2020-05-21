def   RegEx ( _txt , _regex ):
    coincidencia  =  re . partido ( _regex , _txt )
    return   bool ( coincidencia )

def   principal ():
    mientras  que ( Verdadero ):
        LimpiarPantalla ()
        imprimir ( "LISTA DE COTACTOS" )
        imprimir ( "" )
        print ( "[1] Agregar un contacto." )
        print ( "[2] Buscar un contacto." )
        print ( "[3] Eliminar un contacto." )
        print ( "[4] Mostrar contactos." )
        print ( "[5] Serializar datos." )
        print ( "[0] Salir" )
        opcion_elegida   =   input ( "¿Qué deseas hacer?>" )
        si   RegEx ( opcion_elegida , "^ [123450] {1} $" ):
            si   opcion_elegida  ==  "0" :
                imprimir ( "GRACIAS POR UTILIZAR EL PROGRAMA" )
                Rotura
            si   opcion_elegida  ==  "1" :
                imprimir ( "Llamar procedimiento para la acción" )
            si   opcion_elegida  ==  "2" :
                imprimir ( "Llamar procedimiento para la acción" )
            si   opcion_elegida  ==  "3" :
                imprimir ( "Llamar procedimiento para la acción" )
            si   opcion_elegida  ==  "4" :
                imprimir ( "Llamar procedimiento para la acción" )
            si   opcion_elegida  ==  "5" :
                imprimir ( "Llamar procedimiento para la acción" )

            input ( "Pulsa enter para contunuar ..." )
        m á s :
            imprimir ( "Esa respuesta no es válida" )
            input ( "Pulsa enter para contunuar ..." )
 def   CuantosElementosHay ():
    txt   =   "El número de elementos de la colección es {}"
    print ( txt . format ( len ( Contactos )))

def   BuscarTelefono ( telabuscar ):
    coincidencia  =  falso
    para   contacto   en   Contactos :
        if ( contacto . telefono  ==  telabuscar ):
            coincidencia  =  verdadero
            Rotura
    volver   coincidencia

def   BuscarContacto ( telabuscar ):
    contador  =  -  1
    indice_retorno  =  -  1
    para   contacto   en   Contactos :
        contador  +  =  1
        if ( contacto . telefono  ==  telabuscar ):
            indice_retorno  =  contador
            Rotura
    return   indice_retorno
Contactos   = []
CuantosElementosHay ()
Contactos . adjuntar ( Contacto ( 1234567890 , "Ivan Muñoz" , "ivancito.m@hotmail.com" ))
CuantosElementosHay ()
Contactos . adjuntar ( Contacto ( 1134567890 , "Jughead Jones" , "jjughead@gmail.com" ))
Contactos . adjuntar ( Contacto ( 1114567890 , "Selena Gomez" , "sele.nagg@hotmail.com" ))
CuantosElementosHay ()
para   contacto   en   Contactos :
    print ( "------------------------------------------" )
    imprimir ( contacto . telefono )
    imprimir ( contacto . nombre )
    imprimir ( contacto . correo )
    imprimir ( contacto . registro )
    imprimir ( contacto . UIValido )

# Búsqueda de objeto y retorno de índice, usando función de
# búsqueda.
imprimir ( BuscarContacto ( 1234567890 ))
imprimir ( BuscarContacto ( 9999999999 ))

indice_obtenido  =  BuscarContacto ( 1234567890 )
si   indice_obtenido  ==  -  1 :
    print ( "No se encontró el objeto" )
m á s :
    print ( Contactos [ indice_obtenido ]. telefono )
    print ( Contactos [ indice_obtenido ]. nombre )
    print ( Contactos [ indice_obtenido ]. correo )

indice_obtenido  =  BuscarContacto ( 9999999999 )
si   indice_obtenido  ==  -  1 :
    print ( "No se encontró el objeto" )
m á s :
    print ( Contactos [ indice_obtenido ]. telefono )
    print ( Contactos [ indice_obtenido ]. nombre )
    print ( Contactos [ indice_obtenido ]. correo )
