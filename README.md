# Mi primer proyecto en Python "Calculdora de IMC"
Hola, soy Victor Sebastian Rosales Sánchez, y este es mi primer proyecto en Python.

## ¿Qué es necesario?
* Contar con una computadora/laptop y conexión a internet.
* Tener instalada la última versión de Python.
* Emplear Visual Studio Code como editor de texto.
* Tener descargado Git y vincular nuestro editor de texto a éste.

## Descripción del proyecto
Para poder realizar el cálculo del IMC, es necesario contar con una fórmula, la cual especifique los datos requeridos y el tratamiento matemático que permita
llegar al resultado correcto. 

Para esto, se consultó la página oficial del ISSSTE, la cual indica que se debe dividir el peso del individuo (en kilogramos) entre su estatura elevada al 
cuadrado (en metros).

Por lo tanto, para poder realizar los cálculos es necesario pedirle la siguiente información al usuario:
* Nombres(s) y Apellido(s) en variables distintas
(_Para hacer más personal el uso del programa_).
* Edad (_Para poder corroborar si es o no mayor de edad, de forma que se eviten problemas legales y salud_).
* Peso en kilogramos (_Con una variable de tipo float, ya que el peso en kilogramos puede incluir decimales_).
* Estatura en metros (_Con una variable de tipo float, ya que la estatura en metros puede incluir decimales_).

**_Es importante resaltar que estas variables deben de incluir la función input ( ), de forma que el usuario sea capaz de ingresar sus datos y estos se almacenen en variables
que posteriormente serán usadas pra realizar los cálculos correspondientes_**

Previo al cálculo del IMC, es necesario determinar si el usuario es mayor de edad, por lo que se debe emplear la variable en donde este registró su edad, y emplear la
función _if ( )_, de forma que si el usuario es mayor de edad el programa continue, pero si no es así, que el programa se detenga y le indique que no puede realizar el cálculo
cálculo solicitado debido a su edad.

Posteriormente, se debe proceder a realizar los cálculos correspondientes con las variables ingresadas por el usuario:

IMC = peso / (altura**2)

IMC = w / (h**2)

Para complementar el cálculo del IMC y proporcionarle al usuario su estado de salud, se debe emplear la función if ( ) y elif ( ), de forma que usando condicionales
y rangos para el IMC, se le indique al usuario si presenta delgadez u obesidad, y si es así, en qué grado se encuentra. 

Una vez proyectado el nombre del usuario, su IMC (con dos decimales) y estado de salud, se procede  realizar la despedida del programa y darle las gracias por emplearlo. 

## ¿Qué me ha dejado el BootCamp?
Desde hace tiempo el comprender cómo tienen origen los programas y aplicaciones, y la forma en que estos operan, me ha llamado mucho la atención. Hasta el momento, 
el BootCamp de fundamentos en Python me ha permitido analizar y comprender las bases de la programación en Python, cómo funcionan sus variables, funciones y cadenas 
de texto, al grado de saber aplicar toda esa información y ser capaz de comenzar a realizar mis primeros programas, que si bien son sencillos, me dan un alto grado 
de satisfacción, ya que me hacen sentir que voy por el camino correcto y me motivan a seguir aprendiendo. 
