
# Diccionarios -------------------------------------------------------------------------------------------------
ascii_256 = {
    '\x00': 0, '\x01': 1, '\x02': 2, '\x03': 3, '\x04': 4, '\x05': 5, '\x06': 6, '\x07': 7,
    '\x08': 8, '\t': 9, '\n': 10, '\x0b': 11, '\x0c': 12, '\r': 13, '\x0e': 14, '\x0f': 15,
    '\x10': 16, '\x11': 17, '\x12': 18, '\x13': 19, '\x14': 20, '\x15': 21, '\x16': 22, '\x17': 23,
    '\x18': 24, '\x19': 25, '\x1a': 26, '\x1b': 27, '\x1c': 28, '\x1d': 29, '\x1e': 30, '\x1f': 31,
    ' ': 32, '!': 33, '"': 34, '#': 35, '$': 36, '%': 37, '&': 38, "'": 39,
    '(': 40, ')': 41, '*': 42, '+': 43, ',': 44, '-': 45, '.': 46, '/': 47,
    '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55,
    '8': 56, '9': 57, ':': 58, ';': 59, '<': 60, '=': 61, '>': 62, '?': 63,
    '@': 64, 'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72,
    'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80,
    'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88,
    'Y': 89, 'Z': 90, '[': 91, '\\': 92, ']': 93, '^': 94, '_': 95, '`': 96,
    'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104,
    'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112,
    'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120,
    'y': 121, 'z': 122, '{': 123, '|': 124, '}': 125, '~': 126, '\x7f': 127,
    'Ç': 128, 'ü': 129, 'é': 130, 'â': 131, 'ä': 132, 'à': 133, 'å': 134, 'ç': 135,
    'ê': 136, 'ë': 137, 'è': 138, 'ï': 139, 'î': 140, 'ì': 141, 'Ä': 142, 'Å': 143,
    'É': 144, 'æ': 145, 'Æ': 146, 'ô': 147, 'ö': 148, 'ò': 149, 'û': 150, 'ù': 151,
    'ÿ': 152, 'Ö': 153, 'Ü': 154, '¢': 155, '£': 156, '¥': 157, '₧': 158, 'ƒ': 159,
    'á': 160, 'í': 161, 'ó': 162, 'ú': 163, 'ñ': 164, 'Ñ': 165, 'ª': 166, 'º': 167,
    '¿': 168, '⌐': 169, '¬': 170, '½': 171, '¼': 172, '¡': 173, '«': 174, '»': 175,
    '░': 176, '▒': 177, '▓': 178, '│': 179, '┤': 180, 'Á': 181, 'Â': 182, 'À': 183,
    '©': 184, '╣': 185, '║': 186, '╗': 187, '╝': 188, '¢': 189, '¥': 190, '┐': 191,
    '└': 192, '┴': 193, '┬': 194, '├': 195, '─': 196, '┼': 197, 'ã': 198, 'Ã': 199,
    '╚': 200, '╔': 201, '╩': 202, '╦': 203, '╠': 204, '═': 205, '╬': 206, '¤': 207,
    'ð': 208, 'Ð': 209, 'Ê': 210, 'Ë': 211, 'È': 212, 'ı': 213, 'Í': 214, 'Î': 215,
    'Ï': 216, '┘': 217, '┌': 218, '█': 219, '▄': 220, '¦': 221, 'Ì': 222, '▀': 223,
    'Ó': 224, 'ß': 225, 'Ô': 226, 'Ò': 227, 'õ': 228, 'Õ': 229, 'µ': 230, 'þ': 231,
    'Þ': 232, 'Ú': 233, 'Û': 234, 'Ù': 235, 'ý': 236, 'Ý': 237, '¯': 238, '´': 239,
    '≡': 240, '±': 241, '‗': 242, '¾': 243, '¶': 244, '§': 245, '÷': 246, '¸': 247,
    '°': 248, '¨': 249, '·': 250, '¹': 251, '³': 252, '²': 253, '■': 254, '\xa0': 255
}

base64_dict = {
    'A': 0,  'B': 1,  'C': 2,  'D': 3,  'E': 4,  'F': 5,  'G': 6,  'H': 7,
    'I': 8,  'J': 9,  'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,
    'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
    'Y': 24, 'Z': 25,

    'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31,
    'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37,
    'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43,
    's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49,
    'y': 50, 'z': 51,

    '0': 52, '1': 53, '2': 54, '3': 55, '4': 56,
    '5': 57, '6': 58, '7': 59, '8': 60, '9': 61,

    '+': 62, '/': 63
}

## Helpers -------------------------------------------------------------------------------------------------
# A la función le entra un número y lo convierte a binario con el algoritmó básico 
def num_to_binario(num):
    if num == 0:
        return "0"
    bits = []
    while num > 0:
        bits.append(str(num % 2))
        num //= 2
    bits.reverse()
    bits = ''.join(bits).zfill(8)
    return bits

def binario_to_num(binario):
    return int(binario, 2)

def binario_to_decimal(bin_str: str) -> int:
    # Limpia espacios y valida que solo haya 0/1
    b = ''.join(c for c in bin_str.strip() if c in '01')
    print(b)
    valor = 0
    n = len(b)
    for i, bit in enumerate(b):
        if bit == '1':
            valor += 2 ** (n - 1 - i)
    return valor

# Conversores -------------------------------------------------------------------------------------------------

# Conversor binario-texto y texto-binario----------------------------------------------------------------------

# Convierte texto a binario, va caracter por caracter y luego obtiene el valor en ASCII con el diccionario y 
# luego con la función lo pasa a binario y acumula los binarios en la var binario
def text_to_binario(texto):
    binario = ''
    for char in texto:
        ascii_val = ascii_256.get(char, 0)  # Obtener el valor ASCII, 0 si no se encuentra
        bin_char = num_to_binario(ascii_val)
        binario += bin_char + ' '  # Separar los binarios con un espacio
    return binario.strip()  # Eliminar el espacio final

# Convierte binario a texto, primero separa por espacios para jalar los binarios y luego ya separados cada uno  
# lo pasa a número normal y luego lo busca en el diccionario para obtener el caracter correspondiente y lo guarda en la var texto
def binario_to_text(binario):
    texto = ''
    binarios = binario.split(' ')
    for bin_char in binarios:
        ascii_val = binario_to_num(bin_char)
        for char, val in ascii_256.items():
            if val == ascii_val:
                texto += char
                break
    return texto

# Conversor base64-texto y texto-base64----------------------------------------------------------------------

def text_to_base64(texto):
    base64_inv = {v:k for k,v in base64_dict.items()}
    base64_str = ''
    binario_completo = ''
    # Convertimos los caracteres a su representación numérica Asciia
    for char in texto:
        ascii_val = ascii_256.get(char, 0)
        # Convertimos el número Ascii a binario
        binary_val = num_to_binario(ascii_val)
        binario_completo+= binary_val
    while len(binario_completo) % 6 != 0:
        binario_completo += '0'  # Rellenar con ceros para completar bloques de 6 bits
    # Agrupar en bloques de 6 bits
    binario_completo = [binario_completo[i:i+6] for i in range(0, len(binario_completo), 6)]
    # Convertir bloques a base 64
    for bloque in binario_completo:
        num= binario_to_decimal(bloque)
        print(num)
        base64_str+=base64_inv.get(num,'') + ' '
    return base64_str

def base64_to_text(base64_str):
    texto = ''
    binario_completo = ''
    # Convertimos los caracteres a su representación numérica Asciia
    for char in base64_str:
        # Convertimos el char ascci a número base64
        base64_val = base64_dict.get(char, 0)
        # Convertimos el número base64 a binario
        binary_val = num_to_binario(base64_val)
        binary_val = binary_val[2:] # Le quitamos 2 bits porque la función me devuelve 8 bits y en base64 solo ocupamos 6
        binario_completo += binary_val
    # Agrupar en bloques de 8 bits
    binario_completo = [binario_completo[i:i+8] for i in range(0, len(binario_completo), 8)]
    # Convertir bloques a texto
    for bloque in binario_completo:
        texto += binario_to_text(bloque)
    return texto

# Conversor base64-binario y binario-base64----------------------------------------------------------------------
def base64_to_binario(base64_str):
    binario_completo = ''
    # Convertimos los caracteres a su representación numérica Asciia
    for char in base64_str:
        # Convertimos el char ascci a número base64
        base64_val = base64_dict.get(char, 0)
        # Convertimos el número base64 a binario
        binary_val = num_to_binario(base64_val)
        #binary_val = binary_val[2:] # Le quitamos 2 bits porque la función me devuelve 8 bits y en base64 solo ocupamos 6
        binario_completo += binary_val +" "
    return binario_completo

def binario_to_base64(binario):
    base64_inv = {v:k for k,v in base64_dict.items()}
    binario_completo = binario.split(' ')
    base64_str = ''
    # Convertir bloques a base 64
    for bloque in binario_completo:
        num= binario_to_decimal(bloque)
        print(num)
        base64_str+=base64_inv.get(num,'') + ' '
    return base64_str

def xor_binario(binario: str) -> str:
    b = ''.join(c for c in binario if c in '01')
    resultado = ''
    for bit in b:
        # XOR con 1
        if bit == '1':
            resultado += '0'
        else:
            resultado += '1'
    if len(resultado) % 8 == 0:
        resultado = ' '.join(
            resultado[i:i+8] for i in range(0, len(resultado), 8)
        )

    return resultado

# Menú en consola ------------------------------------------------------------------------------------------
def menu():
    while True:
        print("\n==================== MENÚ ====================")
        print("1) ASCII  -> BINARIO")
        print("2) BINARIO -> ASCII")
        print("3) ASCII  -> BASE64 (pasando por BINARIO)")
        print("4) BASE64 -> ASCII (pasando por BINARIO)")
        print("5) BASE64 -> BINARIO")
        print("6) BINARIO -> BASE64")
        print("7) XOR (BINARIO XOR BINARIO)")
        print("0) Salir")
        print("=============================================")

        op = input("Elige una opción: ").strip()

        try:
            if op == "1":
                texto = input("Ingresa texto ASCII: ")
                print("Resultado BINARIO:", text_to_binario(texto))

            elif op == "2":
                b = input("Ingresa binario (con espacios): ")
                print("Resultado ASCII:", binario_to_text(b))

            elif op == "3":
                texto = input("Ingresa texto ASCII: ")
                print("Resultado BASE64:", text_to_base64(texto))

            elif op == "4":
                b64 = input("Ingresa BASE64: ")
                # pasa por binario internamente
                print("Resultado ASCII:", base64_to_text(b64))

            elif op == "5":
                b64 = input("Ingresa BASE64: ")
                print("Resultado BINARIO:", base64_to_binario(b64))

            elif op == "6":
                b = input("Ingresa BINARIO (con espacios): ")
                print("Resultado BASE64:", binario_to_base64(b))

            elif op == "7":
                b1 = input("Ingresa BINARIO: ")
                xor_binario1 = xor_binario(b1)
                print("Resultado XOR de BINARIO:", xor_binario1)
            elif op == "0":
                print("Saliendo...")
                break

            else:
                print("Opción inválida. Intenta de nuevo.")

        except Exception as e:
            print("Error:", e)

# Función principal para probar las conversiones
def main():
    texto = "Hola, Mundo!"
    print("Texto original:", texto)

    binario = text_to_binario(texto)
    print("Texto a binario:", binario)

    texto_recuperado = binario_to_text(binario)
    print("Binario a texto:", texto_recuperado)

if __name__ == "__main__":
    menu()