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

ascii_inv = {v: k for k, v in ascii_256.items()}


## Helpers -------------------------------------------------------------------------------------------------
# Pasa de texto a lista de bytes con ascii_256
def text_to_bytes_ascii256(texto: str):
    out = []
    for ch in texto:
        if ch not in ascii_256:
            raise ValueError(f"Caracter no mapeado en ascii_256: {repr(ch)}")
        out.append(ascii_256[ch])
    return out

# Pasa de lista de bytes a texto con ascii_inv
def bytes_to_text_ascii256(byte_list):
    out = ""
    for b in byte_list:
        if b < 0 or b > 255:
            raise ValueError("Byte fuera de rango 0..255")
        if b not in ascii_inv:
            raise ValueError(f"Byte sin mapeo invertido: {b}")
        out += ascii_inv[b]
    return out

# Hace el XOR de dos listas de bytes
def xor_bytes_lists(a, b):
    if len(a) != len(b):
        raise ValueError("Para XOR, ambas listas deben tener el mismo largo")
    out = []
    for i in range(len(a)):
        out.append(a[i] ^ b[i])
    return out

# Transformaciones HEX a bytes y viceversa

HEX_CHARS = "0123456789ABCDEF"

def byte_to_hex2(n: int) -> str:
    if n < 0 or n > 255:
        raise ValueError("byte_to_hex2 espera 0..255")
    hi = n // 16
    lo = n % 16
    return HEX_CHARS[hi] + HEX_CHARS[lo]


def hex2_to_byte(h1: str, h2: str) -> int:
    def val(c):
        c = c.upper()
        if c in "0123456789":
            return ord(c) - ord('0')
        if c in "ABCDEF":
            return 10 + (ord(c) - ord('A'))
        raise ValueError(f"Hex inválido: {c}")

    return val(h1) * 16 + val(h2)


def bytes_to_hex(byte_list) -> str:
    s = ""
    for b in byte_list:
        s += byte_to_hex2(b)
    return s


def hex_to_bytes(hex_str: str):
    h = "".join(ch for ch in hex_str.strip() if ch != " ")
    if len(h) % 2 != 0:
        raise ValueError("Hex inválido: longitud impar")
    out = []
    for i in range(0, len(h), 2):
        out.append(hex2_to_byte(h[i], h[i+1]))
    return out


# PRNG para generar llaves dinámicas

# Semilla a partir de texto ASCII (guarda bytes cin mod 2^32)
def _seed_from_ascii_text(seed_text: str) -> int:
    sbytes = text_to_bytes_ascii256(seed_text)
    seed = 0
    for b in sbytes:
        seed = (seed * 131 + b) % (2**32)
    if seed == 0:
        seed = 1
    return seed

# LCG state' = (a*state + c) mod 2^32
def lcg_next(state: int) -> int:
    a = 1664525
    c = 1013904223
    m = 2**32
    return (a * state + c) % m

# Genera n bytes ALEATORIOS usando LCG
def prng_bytes(seed: int, n: int):
    out = []
    state = seed
    for _ in range(n):
        state = lcg_next(state)
        out.append(state % 256)
    return out


# Generación de llaves dinámicas ASCII -------------------------------------------------------------------

def generar_llave_dinamica_ascii(longitud: int, seed_text: str):
    if longitud <= 0:
        raise ValueError("La longitud debe ser > 0")
    seed = _seed_from_ascii_text(seed_text)
    key_bytes = prng_bytes(seed, longitud)
    return bytes_to_text_ascii256(key_bytes)


# Stream cipher con llave k (repite la k hasta el tamaño del mensaje) ---------------------------------------
def keystream_llave_fija(key_text: str, n: int):
    k = text_to_bytes_ascii256(key_text)
    if len(k) == 0:
        raise ValueError("Llave fija vacía")
    out = []
    i = 0
    while len(out) < n:
        out.append(k[i % len(k)])
        i += 1
    return out

# Cifra y devuelve ciphertext en HEX
def cifrar_k_fija_hex(plaintext: str, key_text: str) -> str:
    pt = text_to_bytes_ascii256(plaintext)
    ks = keystream_llave_fija(key_text, len(pt))
    ct = xor_bytes_lists(pt, ks)
    return bytes_to_hex(ct)


def descifrar_k_fija_hex(cipher_hex: str, key_text: str) -> str:
    ct = hex_to_bytes(cipher_hex)
    ks = keystream_llave_fija(key_text, len(ct))
    pt = xor_bytes_lists(ct, ks)
    return bytes_to_text_ascii256(pt)


# Stream cipher con llave k dinámica (keystream del tamaño del mensaje) ---------------------------------------

def keystream_dinamico(master_key_text: str, nonce_text: str, n: int):
    seed = _seed_from_ascii_text(master_key_text + "|" + nonce_text)
    return prng_bytes(seed, n)


def cifrar_k_dinamica_hex(plaintext: str, master_key_text: str, nonce_text: str) -> str:
    pt = text_to_bytes_ascii256(plaintext)
    ks = keystream_dinamico(master_key_text, nonce_text, len(pt))
    ct = xor_bytes_lists(pt, ks)
    return bytes_to_hex(ct)


def descifrar_k_dinamica_hex(cipher_hex: str, master_key_text: str, nonce_text: str) -> str:
    ct = hex_to_bytes(cipher_hex)
    ks = keystream_dinamico(master_key_text, nonce_text, len(ct))
    pt = xor_bytes_lists(ct, ks)
    return bytes_to_text_ascii256(pt)


# Menú en consola ------------------------------------------------------------------------------------------

def menu():
    while True:
        print("\n==================== STREAM CIPHER (MANUAL) ====================")
        print("1) Generar llave dinámica ASCII (texto) desde una semilla")
        print("2) Cifrar  (k fija)    -> ciphertext HEX (ASCII)")
        print("3) Descifrar(k fija)    -> plaintext")
        print("4) Cifrar  (k dinámica) -> ciphertext HEX (ASCII)")
        print("5) Descifrar(k dinámica) -> plaintext")
        print("0) Salir")
        print("=================================================================")

        op = input("Elige una opción: ").strip()

        try:
            if op == "1":
                seed_text = input("Ingresa semilla (texto ASCII-256 según tu diccionario): ")
                longitud = int(input("Longitud de llave a generar: ").strip())
                llave = generar_llave_dinamica_ascii(longitud, seed_text)
                print("Llave dinámica generada:")
                print(llave)

            elif op == "2":
                pt = input("Plaintext: ")
                k = input("Llave fija (k): ")
                ct_hex = cifrar_k_fija_hex(pt, k)
                print("Ciphertext (HEX ASCII):")
                print(ct_hex)

            elif op == "3":
                ct_hex = input("Ciphertext HEX: ")
                k = input("Llave fija (k): ")
                pt = descifrar_k_fija_hex(ct_hex, k)
                print("Plaintext:")
                print(pt)

            elif op == "4":
                pt = input("Plaintext: ")
                master = input("Master key: ")
                nonce = input("Nonce (recomendado distinto por mensaje): ")
                ct_hex = cifrar_k_dinamica_hex(pt, master, nonce)
                print("Ciphertext (HEX ASCII):")
                print(ct_hex)

            elif op == "5":
                ct_hex = input("Ciphertext HEX: ")
                master = input("Master key: ")
                nonce = input("Nonce: ")
                pt = descifrar_k_dinamica_hex(ct_hex, master, nonce)
                print("Plaintext:")
                print(pt)

            elif op == "0":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    menu()
