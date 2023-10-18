# Tarea1_Algoritmos


## Descripción

Este proyecto se centra en la multiplicacion de polinomios por medio de dos metodos:
1) Directo 
2) Utilizando la transformada rápida de Fourier.

El programa debe recibir un archivo de texto con dos columnas que tengan los coeficientes de los dos polinomios a multiplicar. Por ejemplo, para multiplicar los siguientes polinomios:

* Polinomio 1: $6x^3 + 7x^2 - 10x^1 + 9x^0$
* Polinomio 2: $-2x^3 + 4x^1 - 5x^0$

El archivo correspondiente deber ser:

```
9 -5
-10 4
7 0
6 -2
```

## Características

- Multiplicacion de polinomios por cualquiera de los dos metodos
- Generacion aletoria de polinomios de acuerdo a un grado dado por el usuario


## Uso

### Primera forma:

Para el caso de este punto se puede correr dos maneras diferentes:

- Por un lado, de la siguiente manera en consola:
```bash
python "$Path_archivo_python/polinomio_mult.py" "$Path_archivo_datos"
```
Aqui, una vez se corra, va a salir como input lo siguiente, donde debe ser seleccionado (1):

```bash
Subio un archivo con el polinomio (1) o desea generar un polinomio (2): 1
```

Posteriormente saldrá como input lo siguiente, donde puede seleccionar 1 o 2 dependiendo de su eleccion:
```bash
Subio un archivo con la matriz (1) o desea generar un grafo (2): 1
```

El resultado a continuacion será algo del estilo:
```bash
Primer polinomio:
6x^3 + 7x^2 + -10x^1 + 9x^0
Segundo polinomio:
-2x^3 + 4x^1 + -5x^0
Resultado
-12x^6 + -14x^5 + 44x^4 + -20x^3 + -75x^2 + 86x^1 + -45x^0
```

- El segundo caso es cuando se quiere generar un nuevo polinomio. Para esto, una vez se corra aparecera en consola lo siguiente, donde debe ser seleccionado el 2:

```bash
Subio un archivo con el polinomio (1) o desea generar un polinomio (2): 2
```

Posteriormente saldra como input lo siguiente, a lo que se debe responder el grado de los polinomios que se desean generar:

```bash
Subio un archivo con el polinomio (1) o desea generar un polinomio (2): 100
```

Finalmente, se va a preguntar por el algoritmo que se desea correr y funciona igual que en el primer caso.