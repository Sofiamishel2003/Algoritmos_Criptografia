

# 1) Cifrado César
ALFABETO_MAY = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
ALFABETO_MIN = "abcdefghijklmnñopqrstuvwxyz"

def cesar_cifrar(mensaje: str, desplazamiento: int) -> str:
    cifrado = ""
    n= len(ALFABETO_MAY)
    shift = desplazamiento % n  # Asegura que el desplazamiento esté dentro del rango del alfabeto
    for char in mensaje:
        if char in ALFABETO_MAY:
            idx = ALFABETO_MAY.index(char)
            nuevo_idx = (idx + shift) % n
            cifrado += ALFABETO_MAY[nuevo_idx]
        elif char in ALFABETO_MIN:
            idx = ALFABETO_MIN.index(char)
            nuevo_idx = (idx + shift) % n
            cifrado += ALFABETO_MIN[nuevo_idx]
        else:
            cifrado += char  # No modificar caracteres no alfabéticos
    return cifrado
def cesar_descifrar(mensaje: str, desplazamiento: int) -> str:
    # Descifrar = cifrar con desplazamiento negativo
    return cesar_cifrar(mensaje, -desplazamiento)

def rot13(mensaje: str) -> str:
    return cesar_cifrar(mensaje, 13)
def menu():
    while True:
        print("\n================== CIFRADOS HISTÓRICOS ==================")
        print("1) César cifrar")
        print("2) César descifrar")
        print("3) ROT13")
        print("4) Vigenère cifrar")
        print("5) Vigenère descifrar")
        print("6) Análisis de frecuencias")
        print("0) Salir")
        print("=========================================================")
        op = input("Elige una opción: ").strip()

        try:
            if op == "1":
                msg = input("Mensaje: ")
                d = int(input("Desplazamiento (int): ").strip())
                print("Cifrado:", cesar_cifrar(msg, d))

            elif op == "2":
                msg = input("Mensaje: ")
                d = int(input("Desplazamiento (int): ").strip())
                print("Descifrado:", cesar_descifrar(msg, d))

            elif op == "3":
                msg = input("Mensaje: ")
                print("ROT13:", rot13(msg))

            elif op == "4":
                msg = input("Mensaje: ")
                key = input("Clave alfabética: ")
                #print("Cifrado:", vigenere_cifrar(msg, key))

            elif op == "5":
                msg = input("Mensaje: ")
                key = input("Clave alfabética: ")
                #print("Descifrado:", vigenere_descifrar(msg, key))

            elif op == "6":
                msg = input("Mensaje: ")
                #tabla = analisis_frecuencia(msg)
                #imprimir_tabla_frecuencia(tabla)

            elif op == "0":
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    menu()
