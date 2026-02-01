# 🔐 Stream Cipher Manual en ASCII

## 📌 Descripción general

Este proyecto implementa un **stream cipher completamente manual en Python**, sin utilizar librerías criptográficas, de codificación ni de generación aleatoria externas.
Todo el procesamiento se realiza **a nivel ASCII (0–255)** utilizando diccionarios explícitos y operaciones básicas como **XOR**, conversión numérica y generación pseudoaleatoria manual.

El objetivo es **comprender el funcionamiento interno de los cifrados por flujo (stream ciphers)** y la diferencia práctica entre el uso de **llaves fijas** y **llaves dinámicas**.


---

## 🏗️ Estructura del sistema

### 1️⃣ Diccionario ASCII 256

Se define manualmente un diccionario `ascii_256` que mapea cada carácter a un valor entre `0–255`, junto con su inverso para reconstrucción del texto.

Esto permite:

* Control total del encoding.
* Evitar dependencias del encoding interno de Python.

---

### 2️⃣ Conversión texto ↔ bytes ASCII

El texto se convierte en listas de enteros (bytes) usando el diccionario ASCII, y viceversa.

---

### 3️⃣ Operación XOR

El cifrado se basa en la operación:

```
cipher_byte = plaintext_byte XOR keystream_byte
```

La misma operación se utiliza para descifrar, ya que:

```
plaintext = cipher XOR keystream
```

---

## 🔑 Tipos de llaves implementadas

### 🔹 Llave fija (k fija)

* La llave tiene un **tamaño fijo**.
* Se **repite** hasta cubrir el tamaño del mensaje.
* El keystream se forma repitiendo la llave.

📌 **Ejemplo conceptual**

```
Mensaje: 10 bytes
Llave k: 3 bytes → ABC
Keystream: ABCABCABCA
```


---

### 🔹 Llave dinámica (k dinámica)

* Se usa una **master key** + un **nonce**.
* A partir de ambos se genera un **keystream único por mensaje**.
* El keystream tiene exactamente el tamaño del mensaje.

---

## 🔄 Generación aleatoria

Se utiliza un **LCG (Linear Congruential Generator)** implementado desde cero para generar bytes pseudoaleatorios.

Esto permite:

* Generar llaves dinámicas.
* Generar keystreams reproducibles (para descifrar).


---

## 🔢 Representación del Ciphertext

El ciphertext se representa en **HEX manual**, lo que garantiza que:

* Solo se usen caracteres ASCII (`0–9`, `A–F`).
* El resultado sea imprimible, transportable y visible.

Ejemplo:

```
0454324460D31B471022
```

---

## 🧪 Funcionalidades del menú

Al ejecutar el programa, se muestra un menú interactivo:

```
1) Generar llave dinámica ASCII
2) Cifrar (k fija) → ciphertext HEX
3) Descifrar (k fija)
4) Cifrar (k dinámica) → ciphertext HEX
5) Descifrar (k dinámica)
0) Salir
```

Cada opción demuestra una parte del funcionamiento del stream cipher.
