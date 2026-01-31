# 🔐 Conversor ASCII, Binario, Base64 y XOR en Python

Este proyecto implementa un **script en Python** que permite realizar conversiones entre **ASCII, binario y Base64**, además de aplicar la operación **XOR** sobre un binario.
El enfoque es **didáctico y matemático**, evitando funciones internas de alto nivel para mostrar explícitamente cómo funcionan las transformaciones binarias.

---

## 📌 Funcionalidades

El programa ofrece las siguientes operaciones a través de un **menú interactivo en consola**:

1. **ASCII → Binario**
   Convierte texto ASCII a su representación binaria de 8 bits por carácter.

2. **Binario → ASCII**
   Convierte binario (en bloques de 8 bits) de regreso a texto ASCII.

3. **ASCII → Base64 (pasando por Binario)**
   Implementación manual del proceso:

   * ASCII → Binario (8 bits)
   * Agrupación en bloques de 6 bits
   * Conversión a Base64 usando tabla de codificación

4. **Base64 → ASCII (pasando por Binario)**
   Proceso inverso:

   * Base64 → valores numéricos
   * Conversión a binario de 6 bits
   * Reconstrucción en bloques de 8 bits
   * Decodificación ASCII

5. **Base64 → Binario**
   Convierte directamente caracteres Base64 a binario.

6. **Binario → Base64**
   Convierte bloques binarios a su representación Base64.

7. **XOR sobre un Binario**
   Aplica la operación XOR **bit a bit** sobre un binario usando una **máscara fija de 1**, invirtiendo cada bit.

---

## 🧠 Enfoque Teórico

### Conversión Binaria

Las conversiones se realizan usando principios matemáticos básicos:

* **Decimal a binario** mediante divisiones sucesivas entre 2.
* **Binario a decimal** usando la suma ponderada de potencias de 2.

### Base64

El algoritmo Base64 se implementa sin librerías externas:

* Se trabaja directamente con bloques de **6 bits**
* Se utilizan diccionarios explícitos de mapeo Base64

### XOR

La operación XOR se define como:

| Bit | XOR 1 |
| --- | ----- |
| 0   | 1     |
| 1   | 0     |

Por lo tanto, aplicar XOR con 1 equivale a **invertir el bit**, lo cual es una operación válida y común en criptografía básica.

---

## Ejemplo de XOR

**Entrada:**

```
01001100
```

**Proceso:**

```
0 ⊕ 1 = 1
1 ⊕ 1 = 0
0 ⊕ 1 = 1
0 ⊕ 1 = 1
1 ⊕ 1 = 0
1 ⊕ 1 = 0
0 ⊕ 1 = 1
0 ⊕ 1 = 1
```

**Salida:**

```
10110011
```

---

## ▶️ Cómo ejecutar el programa

1. Asegúrate de tener **Python 3.10 o superior**
2. Ejecuta el archivo desde la terminal:

```bash
python Conversor.py
```

3. Usa el menú interactivo para seleccionar la operación deseada.

---

## 📂 Estructura del código

* **Diccionarios**

  * `ascii_256`: tabla ASCII extendida (0–255)
  * `base64_dict`: tabla Base64 estándar

* **Funciones auxiliares**

  * `num_to_binario`
  * `binario_to_decimal`
  * `binario_to_num`

* **Conversores**

  * `text_to_binario`
  * `binario_to_text`
  * `text_to_base64`
  * `base64_to_text`
  * `base64_to_binario`
  * `binario_to_base64`

* **Criptografía**

  * `xor_binario`

* **Interfaz**

  * `menu()`

## 👩‍💻 Autora

**Sofía Mishell Velásquez**
