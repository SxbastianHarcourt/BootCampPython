diccionario_ingles = {'rojo' : 'red', 'naranja' : 'orange', 'amarillo' : 'yellow', \
    'verde' : 'green', 'azul' : 'blue', 'violeta' : 'purple'}

diccionario_frances = {'rojo' : 'rouge', 'naranja' : 'orange', 'amarillo' : 'jaune', \
    'verde' : 'vert', 'azul' : 'bleu', 'violeta' : 'violette'}

print ('Bienvenido al traductor de colores. Los idiomas disponibles son: inglés y francés')
idioma = input('Indique el idioma al que quiere traducir: ')
idioma = idioma.lower()
if idioma == 'inglés' :
    texto = input ('Ingrese su oración: ')
    texto = texto.lower()
    palabras = texto.split()
    traduccion = ''
    for palabra in palabras:
        if palabra in diccionario_ingles:
            traduccion = traduccion + diccionario_ingles[palabra] + ' '
        else :
            traduccion = traduccion + palabra + ' '
    print (traduccion)

elif idioma == 'francés' :
    texto = input ('Ingrese su oración: ')
    texto = texto.lower()
    palabras = texto.split()
    traduccion = ''
    for palabra in palabras:
        if palabra in diccionario_frances:
            traduccion = traduccion + diccionario_frances[palabra] + ' '
        else:
            traduccion = traduccion + palabra + ' '
    print(traduccion)
    
else:
    print('La sintaxis es incorrecta o el idioma solicitado no está disponible. Por favor inténtelo de nuevo.')
    exit()
