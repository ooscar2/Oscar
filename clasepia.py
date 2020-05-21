Contacto de clase :
def  __init__ ( self , telefono , nombre , correo , registro = datetime . datetime . now (), UIValido = False ):
    auto . telefono = telefono
    auto . nombre = nombre
    auto . correo = correo
    auto . registro = registro
    auto . UIValido = UIValido

importar  re
# Se importa la clase del Contacto
de  definirclase  import  Contacto

# Validadorcon expresiones regulares
def  RegEx ( _txt , _regex ):
    coincidencia = re . partido ( _regex , _txt )
    return  bool ( coincidencia )

# Expresiones regulares para campos.
telefonoRegEx = "^ [0-9] {10} $"
nombreRegEx = "^ [AZ] + (([',. -] [AZ])? [AZ] *) * $"
entidadValida = Verdadero

# Pregunta num de teléfono.
_telefono = ""
telefono = 0
datoValido = False
mientras  cierto :
    _telefono = input ( "Teléfono:" )
    si  RegEx ( _telefono , telefonoRegEx ):
        telefono = int ( _telefono )
        datoValido = True
        rotura
    más :
        print ( "Se identificaron 10 dígitos como número" )
        datoValido = False
    entidadValida = ( entidadValida  y  datoValido )

# Preguntar nombre.
nombre = ""
datoValido = False
mientras  cierto :
    nombre = input ( "Nombre:" )
    si  RegEx ( nombre , telefonoRegEx ):
        datoValido = True
        rotura
    más :
        print ( "Se requiere nombre, apellido, no mayor a 30 catacteres." )
        datoValido = False
    entidadValida = ( entidadValida  y  datoValido )
