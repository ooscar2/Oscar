# Pregunta diferentes tipos de datos, sin validación.

# se preguntan o se calculan
#datos str, int, float y fechas
#en este caso en notación hungara
# str string
# i int
# f flotante
# fecha dt


def  main ():
 #string convierte cualquier valor a una cadena
 strDato  =  input ( "Dame un dato string:" )
 # Los datos numéricos se preguntan por intermediación.
 _iDato  =  input ( "Dame un dato entero:" )
 iDato  =  int ( _iDato )
 _fDato  =  input ( "Dame un dato float:" )
 fDato  = float ( _fDato )
 # Los datos date se preguntan por intermediación.
 _dtDato  =  input ( "Dame una fecha aaaa / mm / dd:" )
 # para este formato, se debe mandar en el orden correcto para que este funcione

 anio = _dtDato [ 0 : 4 ]
 mes = _dtDato [ 5 : 7 ]
 dia = _dtDato [ - 2 :]
 imprimir ( anio )
 imprimir ( mes )
 imprimir ( dia )

 dtDato  =  datetime . datetime ( int ( anio ), int ( mes ), int ( dia ))

 imprimir ( strDato )
 print ( tipo ( strDato ))
 imprimir ( iDato )
 print ( tipo ( iDato ))
 imprimir ( fDato )
 print ( tipo ( fDato ))
 imprimir ( dtDato )
 print ( tipo ( dtDato ))