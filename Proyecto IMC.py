# Proyecto índice de masa corporal
print('''Bienvenid@ a la calculadora de índice de masa corporal
Por favor registra tus datos''')

n = input('Ingresa tu Nombre: ')
p = input('Ingresa tu Apellido Paterno: ')
m = input('Ingresa tu Apellido Materno: ')
e = int(input('Ingresa tu edad: '))
w = float(input('Ingresa tu peso en kilogramos: '))
h = float(input('Ingresa tu estatura en metros: '))

IMC = w / (h**2)

if (e < 18):
    print('Usted es menor de edad, no puede realizar el cálculo')
    
else:
    print ('Usted es mayor de edad')

    print (str(n) + str (p) + str(m))
    print(f'Tu IMC es {IMC : .2f}')

    # Salud segú el IMC
    if IMC >= 0 and IMC <= 15.99 : 
        print('Usted tiene Delgadez Severa')
    elif IMC >= 16.00 and IMC <= 16.99 :
        print('Usted tiene Delgadez Moderada')
    elif IMC >= 17.00 and IMC <= 18.49 : 
        print('Usted tiene Delgadez Normal')
    elif IMC >= 18.50 and IMC <= 24.99 :
        print('Usted tiene un IMC normal')
    elif IMC >= 25.00 and IMC <= 29.99 :
        print('Usted tiene Soprepeso')
    elif IMC >= 30.00 and IMC <= 34.99 :
        print('Usted tiene obesidad leve')
    elif IMC >= 35.00 and IMC <= 39.00 :
        print('Usted tiene obesidad media')
    elif IMC >= 40.00 :
        print ('Usted tiene obesidad morbida')

print('''
Gracias por usar la calculadora de IMC

Atte. Víctor Sebastián Rosales Sánchez''')
