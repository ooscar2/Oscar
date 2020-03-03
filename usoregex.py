# Pregunta un dato que sea verdadero para que al momento de comparar se compruebe si es verdadero o falso

# Importa el módulo requerido para usar Expresiones regulares.
importar  re

def  main ():
  # se pregunta en este caso el "Rfc" mientras la condicion se cumpla y se compruebe verdadero este se imprime, mientras no se cumpla se comprueba incorrecto  y se vuelve a preguntar
  mientras  cierto :
    strRFC  =  input ( "Dame el RFC:" )
    #en esta parte se comprueba que coinicidan lo que puso el ursuario con la informacion que se tiene 
    coincidir  =  re . búsqueda ( "^ [AZ] {4} - [0-9] {6} - [A-Z0-9] {3} $" , strRFC )
    si ( coincidir ):
      print ( "RFC Correcto!" )
      descanso
    más :
      print ( "RFC incorrecto. Intenta de nuevo." )