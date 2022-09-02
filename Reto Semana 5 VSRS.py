# Reto Semana 5: Sebastian Rosales

año_actual = input("""¡Hola!
Por favor ingresa el año actual: """)

# Condiciones para el año actual

if año_actual.isnumeric() :
    presente = int(año_actual)
else :
    print ('Dato Incorrecto. Por favor ingresa un valor numérico válido.')
    exit ()

if presente < 2022 : # Esta condición puede ser actualizada con el paso de los años.
    print ('No es posible que el año ingresado sea el actual. Por favor ingresa en año correcto.')
else :
    # Condiciones para el año random
    año_random = input('Por favor ingresa otro año para calcular: ')
    if año_random.isnumeric() :
        random = int(año_random)
    else :
        print ('Dato Incorrecto. Por favor ingresa un valor numérico válido')
        exit ()
    
    # Cálculos de años transcurridos
    if random == presente :
            print ('El año ingresado NO puede ser igual al año actual. Por favor ingrese otro año.')
    elif random > presente :
            m = random - presente
            print ('Faltan', m , 'años para el año', random )
    elif random < presente :
            n = presente - random
            print ('Han pasado', n,'años desde el año', random)
