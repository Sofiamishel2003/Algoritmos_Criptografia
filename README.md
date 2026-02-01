# 🔐 Ejercicio de Criptografía

**Lenguaje:** Python

---

## 📌 Descripción general

Este repositorio contiene la solución completa al **Ejercicio de Criptografía**, dividido en **tres partes principales**, cada una implementada en un módulo independiente y documentada mediante su propio `README.md`.

---

## 📂 Estructura del repositorio

```
ALGORITMOS_CRIPTOGRAFIA/
│
├── Criptografia/
│   ├── Conversor.py
│   └── README.md
│
├── Criptografia_Keys/
│   ├── Criptografia_Keys.py
│   └── README.md
│
├── Cifrados_Historicos/
│   ├── cifrados_historicos.py
│   └── README.md
│
└── README.md   ← (este archivo)
```

---

# 🧩 EJERCICIO 1 – Conversión de información y operaciones binarias

📁 **Carpeta:** `Criptografia/`
📄 **Archivo principal:** `Conversor.py`

## 🎯 Objetivo

Implementar manualmente scripts que permitan la conversión entre **ASCII, Binario y Base64**, pasando siempre por representación binaria, y aplicar la operación **XOR**.

## 🔧 Funcionalidades implementadas

* ASCII → Binario
* Binario → ASCII
* ASCII → Base64 (pasando por binario)
* Base64 → ASCII (pasando por binario)
* Base64 → Binario
* Binario → Base64
* XOR aplicado a binarios

Todas las conversiones utilizan:

* Diccionario ASCII de 256 caracteres
* Diccionario Base64
* Algoritmos manuales de conversión binaria

---

# 🧩 EJERCICIO 2 – Criptografía con llaves (Stream Cipher)

📁 **Carpeta:** `Criptografia_Keys/`
📄 **Archivo principal:** `Criptografia_Keys.py`

## 🎯 Objetivo

Implementar un **cifrado tipo Stream Cipher manual**, utilizando ASCII y XOR, con:

* Llave de tamaño fijo
* Llave de tamaño dinámico generada a partir de una semilla

## 🔑 Funcionalidades implementadas

### 1️⃣ Generación de llaves dinámicas

* Llaves generadas en ASCII
* Uso de un PRNG manual (LCG)
* Dependientes de una semilla textual

### 2️⃣ Cifrado con llave fija

* La llave se repite hasta el tamaño del mensaje
* XOR byte a byte
* Salida en formato HEX ASCII

### 3️⃣ Cifrado con llave dinámica

* Keystream del tamaño exacto del mensaje
* Uso de **master key + nonce**
* XOR byte a byte
* Salida en formato HEX ASCII

### 4️⃣ Descifrado

* Totalmente reversible
* Utiliza la misma llave y nonce

---

# 🧩 EJERCICIO 3 – Cifrados Históricos y Criptoanálisis

📁 **Carpeta:** `Cifrados_Historicos/`
📄 **Archivo principal:** `cifrados_historicos.py`

## 🎯 Objetivo

Implementar cifrados históricos clásicos y un análisis básico de criptoanálisis, reutilizando conceptos del ejercicio de criptografía.

## 🔐 Cifrados implementados

### 1️⃣ Cifrado César

* Desplazamiento configurable
* Alfabeto español (incluye Ñ)
* Cifrado y descifrado

### 2️⃣ ROT13

* Caso especial del César
* Reutiliza la lógica del cifrado César

### 3️⃣ Cifrado Vigenère

* Uso de clave alfabética
* Implementación mediante **matriz de Vigenère**
* Cifrado y descifrado completamente reversibles

### 4️⃣ Análisis de frecuencias

* Conteo de caracteres
* Cálculo de porcentajes
* Ordenamiento por frecuencia
* Tabla de resultados para criptoanálisis
