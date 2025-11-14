1. Listas - list<br>
   Las listas en python son colecciones de datos que se crean atraves de corchetes y se separan con comas,
   nos sirven para almacenar multiples datos de distintos tipos como int, strings y booleans.
   Los elementos de la lista se almacenan en una variable a la cual podemos acceder mediante un indice que
   comienza en 0.

1.1 ¿Por qué son mutables?<br>
   Las listas son mutables porque nos permiten modificar tanto sus elementos como su estructura. Esto nos permite
   gestionar colecciones de datos que luego cambian con el tiempo, esto nos permite añadir, eliminar y cambiar
   directamente elementos en la lista existente. 

1.2 Situaciones donde son utiles<br>
    - Cuando necesitamos almacenar datos que con el tiempo debemos de modificar.<br>
    - Cuando necesitamos almacenar datos de diferente tipos como cadenas de textos, numericos, alafanumericos
    o booleanos.

1.3 Ejemplos 

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

2. Tuplas<br>
   Las tuplas son colecciones de datos ordenadas que son inmutables (no se pueden modificar), dentro de ellas
   se pueden almacenar datos de diferentes tipos, al igual que las listas.

2.1 ¿Por qué son inmutables?<br>
   Las tuplas son inmutables porque una vez creadas los elementos que contiene no pueden ser alterados, 
   añadidios o eliminados, esto nos proporciona seguridad t permite utilizarlas como claves (keys) en diccionarios 

2.2 Situaciones donde son utiles<br>
   - Cuando necesitas datos que no varien y sean fijos.
   - Cuando necesitamos usar datos como claves en diccionarios.
   - Cuando necesitas que tu programa sea mas rapido, las tuplas son mas eficientes que las listas.

2.3 Ejemplos

   Acceso
   frutas = ("Manzana". "Pera", "Mango", "Coco")
   print(frutas[0])

   Recorrer 
   frutas = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")
   for fruta in frutas:
      print(fruta)
   

   
      
    
    
    
