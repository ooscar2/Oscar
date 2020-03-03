# se deifne la variable que usa cadenas, para incrustar valores

def  main ():
  #se utiliza el "int" para imprimir valores numericos enteros y el "float" para valores numericos decimales
  intBase  =  7
  intAltura  =  5
  fltAreaTriangulo = ( intBase * intAltura ) / 2
  txt  =  "Área: {2: 0.2f} ({0} por {1} entre dos)"
  print ( formato txt . ( intBase , intAltura , fltAreaTriangulo ))

# se utiliza en esta cadena un parametro de base 0.
#en este la operacion no es flotante 