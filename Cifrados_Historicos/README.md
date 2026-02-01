# 🔐 Cifrados Históricos (César, ROT13, Vigenère y Análisis de Frecuencias)

## 📌 Descripción general

Este proyecto implementa **cifrados históricos clásicos** utilizando Python, sin hacer uso de librerías criptográficas ni funciones nativas de cifrado.
El objetivo principal es **comprender los principios fundamentales de la criptografía**, que sirven como base conceptual de los sistemas modernos.

Los cifrados históricos, aunque inseguros para proteger información real hoy en día, permiten estudiar conceptos clave como:

* Representación de la información
* Transformaciones reversibles
* Confusión y difusión
* Ataques criptográficos básicos
* Criptoanálisis por frecuencia

---

## 🔤 Alfabeto utilizado

Se utiliza el **alfabeto español**, tanto en mayúsculas como en minúsculas:

```python
ALFABETO_MAY = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
ALFABETO_MIN = "abcdefghijklmnñopqrstuvwxyz"
```

Esto permite:

* Cifrar correctamente textos en español.
* Incluir la letra **Ñ** como parte válida del sistema criptográfico.

---

## 1️⃣ Cifrado César

### 📖 Descripción

El cifrado César es un cifrado por sustitución simple en el que cada letra del mensaje se desplaza un número fijo de posiciones dentro del alfabeto.

### 🔁 Características

* El desplazamiento es configurable.
* Se conserva la distinción entre mayúsculas y minúsculas.
* Los caracteres no alfabéticos no se modifican.
* El descifrado se realiza aplicando el desplazamiento inverso.

### 📦 Funciones implementadas

```python
cesar_cifrar(mensaje, desplazamiento)
cesar_descifrar(mensaje, desplazamiento)
```

---

## 2️⃣ ROT13

### 📖 Descripción

ROT13 es un **caso especial del cifrado César**, donde el desplazamiento es fijo e igual a 13 posiciones.

### 🔁 Características

* No duplica lógica.
* Reutiliza directamente la implementación del cifrado César.

### 📦 Función implementada

```python
rot13(mensaje)
```

---

## 3️⃣ Cifrado Vigenère

### 📖 Descripción

El cifrado Vigenère es un cifrado polialfabético que utiliza una **clave alfabética** para determinar el desplazamiento de cada letra del mensaje.

### 🧮 Matriz de Vigenère

Se implementa explícitamente la **tabla o matriz de Vigenère**, donde:

* Cada fila es una rotación del alfabeto.
* La fila se selecciona según la letra de la clave.
* La columna se selecciona según la letra del mensaje.

Esto refleja fielmente el funcionamiento histórico del cifrado.

### 🔁 Características

* La clave se repite solo sobre letras.
* Los espacios y signos de puntuación no se cifran.
* El cifrado y descifrado son completamente reversibles.

### 📦 Funciones implementadas

```python
crear_matriz_vigenere()
vigenere_cifrar(mensaje, clave)
vigenere_descifrar(mensaje, clave)
```

---

## 4️⃣ Análisis de frecuencias

### 📖 Descripción

El análisis de frecuencias es una técnica de **criptoanálisis clásico** utilizada para atacar cifrados por sustitución simple.

Se basa en el hecho de que:

* Las letras no aparecen con la misma frecuencia en un idioma.
* Al cifrar por sustitución, las frecuencias se conservan aunque cambien las letras.

### 🔁 Funcionamiento

* Se analizan únicamente las letras del alfabeto.
* Se normaliza el mensaje a mayúsculas.
* Se calcula:

  * Conteo absoluto de cada letra.
  * Porcentaje relativo.
* Los resultados se ordenan de mayor a menor frecuencia.

### 📦 Funciones implementadas

```python
analisis_frecuencia(mensaje)
imprimir_tabla_frecuencia(tabla)
```

---

## 📋 Menú interactivo

El programa incluye un menú en consola que permite ejecutar todas las funciones:

```
1) César cifrar
2) César descifrar
3) ROT13
4) Vigenère cifrar
5) Vigenère descifrar
6) Análisis de frecuencias
0) Salir
```