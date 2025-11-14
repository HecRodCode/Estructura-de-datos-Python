# 1. Listas - list<br>
   Las listas en python son colecciones de datos que se crean atraves de corchetes y se separan con comas,
   nos sirven para almacenar multiples datos de distintos tipos como int, strings y booleans.
   Los elementos de la lista se almacenan en una variable a la cual podemos acceder mediante un indice que
   comienza en 0.

# 1.1 ¿Por qué son mutables?<br>
   Las listas son mutables porque nos permiten modificar tanto sus elementos como su estructura. Esto nos permite
   gestionar colecciones de datos que luego cambian con el tiempo, nos permite añadir, eliminar y cambiar
   directamente elementos en la lista existente. 

# 1.2 Situaciones donde son utiles<br>
   - Cuando necesitamos almacenar datos que con el tiempo debemos de modificar.<br>
   - Cuando necesitamos almacenar datos de diferente tipos como cadenas de textos, numericos, alafanumericos
   o booleanos.

# 1.3 Ejemplos 

    Creacion:
    nombres = ["Hector Rodriguez", 12, 23, "Santiago Arias", True] 
    
    Leer:
    Frutas = [Manzana, Pera, Piña, Banano]
    print(frutas)

    Modificar:
    vocales = [a, e, i, o, u]
    vocales[3] = h

    Eliminar:
    dias = [Lunes, Martes, Miercoles, Jueves, Viernes]
    dias.remove(Lunes)

# 2. Tuplas - tuples <br>
   Las tuplas son colecciones de datos ordenadas que son inmutables (no se pueden modificar), dentro de ellas
   se pueden almacenar datos de diferentes tipos, al igual que las listas.

# 2.1 ¿Por qué son inmutables?<br>
   Las tuplas son inmutables porque una vez creadas los elementos que contiene no pueden ser alterados, 
   añadidios o eliminados, esto nos proporciona seguridad t permite utilizarlas como claves (keys) en 
   diccionarios 

# 2.2 Situaciones donde son utiles<br>
   - Cuando necesitas datos que no varien y sean fijos.
   - Cuando necesitamos usar datos como claves en diccionarios.
   - Cuando necesitas que tu programa sea mas rapido, las tuplas son mas eficientes que las listas.

# 2.3 Ejemplos

    Acceso:
    frutas = ("Manzana". "Pera", "Mango", "Coco")
    print(frutas[0])

    Recorrer:
    frutas = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")
    for fruta in frutas:
      print(fruta)

# 3. Diccionarios<br>
   Los diccionarios son colecciones mutables y desordenadas que almacenan datos en pares de clave - valor.
   Cada clave, que debe ser inmutable (como cadenas de texto o numeros), se utilizan para acceder a un valor
   asociado, de manera similar a como uno usa una palabra para encontrar su significado en un diccionario.

# 3.1 Diferencia de las claves frente a las tuplas y listas<br>
   - Las listas y tuplas usan índices numéricos posicionales para acceder a la información, mientras que
     los diccionarios usan claves descriptivas.
   - Las listas y diccionarios son mutables, por lo que permiten cambios en su contenido y tamaño despues de
     ser creados. En cambio las tuplas son inmutables; su contenido y tamaño son fijos desde el momento de su
     creación.

# 3.2 Ejemplos

    Creacion:
    contantos = {
       "Juan": 3015542517,
       "Camila": 3144259845,
       "Fernando": 3124857152,
    }

    print(f"Diccionario inicial: {contantos}\n")
   
    Consultar:
    telefono_juan = contactos["Juan"]
    print(f"El telefono de Juan es: {telefono_juan}")

    Agregar:
    contactos["Diana"] = 3561524486
    print(f"Despues de agregar a Diana: {contactos}\n")

    Modificar:
    contactos["Juan"] = 2354859610
    print(f"Despues de modificar el numero de Juan: {contactos}")

    Eliminar:
    del contactos["Fernando"]
    print(f"despues de eliminar a Fernando: {contactos}\n")

# 4. Match-case
   Es una estructura de control de flujo que permite comparar un valor (sujeto) con una serie de patrones
   definidos en los diferentes "case". Cuando el valor conincide con un patron se ejecuta el bloque de codigo
   asociado a ese "case".

# 4.1 ¿Para qué se usa?
   El match/case se utiliza principalmente para mejorar la legibilidad y simplificar la lógica del control de
   flujo.

# 4.2 Difenrencias frente a if/elif<br>
   - El match/case tiene un propósito más orientado a la coincidencia de patrones estructurales, mientras que
     if/elif a evaluar a expresiones lógicas y booleanas.
   - El if/elif ejecuta un bloque si la condición es True, y el match/case ejecuta un bloque si el valor
     coincide con el patrón.
   - Mientras que el if/elif es ideal para lógica condicional simple o compleja, el match/case simplifica la
     lógica con multiples opciones fijas o estructuras de datos.

# 4.3 Situaciones donde usarlo puede ser más claro<br>
   - Cuando tienes un conjunto finito de valores posibles para una variable, match es mas limpio que usar
     multiples elif.
   - match/case es más claro que if/elif cuando se extraen datos de estructuras porque permite
     definir la forma exacta de los datos que se esperan y asigna sus partes a variables automáticamente,
     simplificando la lógica de desempaquetado manual.

# 4.4 Ejemplo<br>

    opcion = int(input("Ingresa un número del 1 al 3: "))
    match opcion:
       case 1:
          print("Elegiste la opción UNO. Iniciando el modo fácil.")
       case 2:
          print("Elegiste la opción DOS. Entrando al menú intermedio.")
       case 3:
          print("Elegiste la opción TRES. Activando el modo difícil.")
       case _:
          print("Número fuera de rango. Por favor, ingresa 1, 2 o 3.")
          
