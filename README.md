# Ejercicio 1 - Generador de secuencias primas grandes

Función principal: `prime_sequence_generator(n: int)`

## Ejecución
La ejecución del script se realiza desde la consola de comandos de la siguiente manera

```
python ejercicio_1 -n 50
```

El resultado de la ejecución del script sería una lista con lo números primos que se encontrado entre 0 y `n`, el cual puede ser modificado con el argumento `-n` desde la consola de comandos. 

## Resultados
El resultado se muestra en consola de la siguiente manera dentro de la consola de comandos.

```
Resultado : [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

# Ejercicio 2 - Decorador para medir el tiempo de ejecución.

Decorador: `timing_decorator`

## Ejecución
Le ejecución del script se realiza desde la consola de comandos de la siguiente manera

```
python ejercicio_2.py -n 10000
```

El script ejecuta una función llamada `calculate_factorial` la cual recibe como parámetro de entrada un valor entre `n` el cual puede ser modificado con el argumento `-n` desde la consola de comandos. 

## Resultados
El resultado se muestra tanto en la consola de comandos como en un archivo .log llamado `execution_times` y se muestra de la siguiente manera.

```
2024-10-26 16:48:40,559 [INFO] 0.001996278762817383
```

# Ejercicio 3 - Metaprogramación - Contador de Instancias

Metaclase: `instance_counter_metaclass`

## Ejecución
La ejecución del script se realiza desde la consola de comandos de la siguiente manera

```
python ejercicio_3.py -l Alice Bob
```

El script crea la cantidad de instancias que haya recibido de la lista `-l`, esta puede variar agregando más nombres separados por un espacio entre cada nombres después del argumento `-l`.

## Resultados
El resultado que muestra en consola es el siguiente

```
Num. Instancias creadas:  2
```

# Ejercicio 4 - Análisis Asincrono de Archivos CSV

Función principal: `async_csv_sum`

## Ejecución
La ejecución del script se realiza de la siguiente maneraÑ

```
python ejercicio_4.py
```

El script analiza los archivo data1.csv y data2.csv dentro de la carpeta resources. Es posible agregar más archivos de lectura siempre que estos solo contengan una columna llamada `value`, sean agregados a la carpeta resources, subcarpeta csv y se agreguen al parámetro `-l` separador por un espacio entre archivo. Tal como se muestra en el siguiete ejemplo.

```
python ejercicio_4.py -l ./resources/csv/data1.csv ./resources/csv/data2.csv
```

Los directorios no deben de incluir espacio ni comillas.

## Resutados
El resultado se muestra en consola de la siguiente manera

```
{'data1.csv': 55, 'data2.csv': 210}
```

# Ejercicio 5 - Testeo Automatizado con Pytest

Función principal: `is_palindrome`

## Validación de palindromos

### Ejecución
Para validar si una palabra es un palíndromo, la ejecución es la siguiente manera

```
python ejercicio_5.py -w radar
```

Por otro lado, si se quiere validar una oración, es necesario agregar comillas dobles al principio y final de la oración, de la siguiente manera

```
python ejercicio_5.py -w "anita lava la tina"
```

### Resultados
Los dos posibles resultados que se pueden obtener de la ejecución es la confirmación o rechazo de que una palabra u oración sea un palidromo, los cuales se ven de la siguiente manera

```
# Cuando la oración o palabra es un palíndromo
La palabra 'anita lava la tina' es palindromo

# Cuando la oración o palabra no es un palíndromo
La palabra 'python' no es palindromo
```

## Testo automatizado

### Ejecución
Para realizar el testeo automatizado de la función se incluyó un archivo test_palindrome.py que se puede ejecutar de la siguiente manera:

```
pytest test_palindrome.py
```

### Resultados
Los resultados deberían mostrarse de la siguiente manera

```
platform win32 -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: C:\Users\lalor\OneDrive\Documents\PythonProjects\quiz_python_avanzado
collected 5 items

test_palindrome.py .....                                                                                         [100%]

================================================== 5 passed in 0.02s ==================================================
```

# Ejercicio 6 - Context Manager Personalizado para Conexión a una Base de Datos

Context Manager: `database_connection_manager`

## Ejecución
La ejecución de este script se realiza llamando al script `ejercicio_6.py` de la siguiente manera

```
python ejercicio_6.py
```

## Resultados
El proceso crea una base de datos en el mismo directorio donde se encuentre ubicado el script llamada `example.db` la cual contiene dos registro que se muestran en consola después de la ejecución.

```
Connection to database 'example.db' open.
Connection to database 'example.db' close.
Connection to database 'example.db' open.
[(1, 'Alice'), (2, 'Bob')]
Connection to database 'example.db' close.
```

# Ejercicio 7 - Procesamiento Paralelo de Archivos de Texto

Función principal: `parallel_word_count`

## Ejecución
El script analiza dos archivos de texto ubicados en la carpeta resources, subcarpeta text. La ejecución del script se realiza de la siguiente manera

```
python ejercicio_7.py
```

Es posible agregar más archivos de validación siempre que sean agregados a la misma carpeta de resources en la subcarpeta text y estos sean agregados en el argumento `-l` de la siguiente manera

```
python ejercicio_7.py -l ./resources/text/file1.txt ./resources/text/file2.txt
```

Los directorios son agregados separados por un espacio y sin comillas de ningun tipo.

## Resultados
El resultado de la ejecución se muestra en consola de la siguiente manera

```
{'file1.txt': 20, 'file2.txt': 21}
```