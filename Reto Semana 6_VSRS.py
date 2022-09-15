# Solicitud de contraseña

password = input ('Ingresa tu contraseña: ')

for i in password :
    if i.isnumeric ():
        confirm = input ('Vuelva a ingresar su contraseña: ')
        if password == confirm :
            print ('Contraseña Correcta.')
            exit ()
        else :
            print ('Las contraseñas no coinciden. Le restan dos intentos.')
            confirm = input ('Confirme su contraseña: ')
            if password == confirm :
                print ('Contraseña Correcta.')
                exit ()
            else :
                print ('Las contraseñas nuevamente no coinciden. Le resta un intento.')
                confirm = input ('Confime su contraseña: ')
                if password == confirm :
                    print ('Contraseña Correcta.')
                    exit ()
                else: 
                    print ('Las contraseñas no coinciden. No le restan intentos.')
                    exit () # Todo hasta este punto es CORRECTO

    else :
        print ('La contraseña debe inciar con un número. Por favor, ingrese de nuevo su contraseña.') # Segundo Intento
        print ('Le restan dos intentos.')

        password = input ('Ingresa tu contraseña: ')
        for i in password :
            if i.isnumeric ():
                confirm = input ('Vuelva a ingresar su contraseña: ')
                if password == confirm :
                    print ('Contraseña Correcta.')
                    exit ()
                else :
                    print ('Las contraseñas no coinciden. Le restan 2 intentos.')
                    confirm = input ('Confirme su contraseña: ')
                    if password == confirm :
                        print ('Contraseña Correcta.')
                        exit ()
                    else :
                        print ('La contraseña nuevamente no coincide. Le resta un intento.')
                        confirm = input ('Confirme su contraseña: ')
                        if password == confirm :
                            print ('Contraseña Correcta.')
                            exit ()
                        else :
                            print ('Las contraseñas contraseñas no coinciden. No le restan intentos.')
                            exit ()
                            
            else :
                print ('La contraseña debe iniciar con un número. Por favor, ingrese de nuevo su contraseña.') # Tercer Intento
                print ('Le resta un intento.')
                password = ('Ingrese su contraseña: ')
                if i.isnumeric ():
                    confirm = input ('Vuelva a ingresar su contraseña: ')
                    if password == confirm :
                        print ('Contraseña Correcta.')
                        exit ()
                    else :
                        print ('La contraseña no coincide. Le restan 2 intentos.')
                        confirm = input ('Vuelva a ingresar su contraseña: ')
                        if password == confirm :
                            print ('Contraseña Correcta.')
                            exit ()
                        else :
                            print ('La contraseña nuevamente no coincide. Le resta 1 intento.')
                            confirm = input ('Vuelva a ingresar su contraseña: ')
                            if password == confirm :
                                print ('Contraseña Correcta.')
                                exit ()
                            else :
                                print ('Las contraseñas no coinciden. No le restan intentos.')
                                exit ()
           