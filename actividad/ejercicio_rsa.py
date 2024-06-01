import random
import sympy
def generar_claves(tamaño_bits):
    # Generar números primos grandes p y q
    p = sympy.randprime(2**(tamaño_bits//2 - 1), 2**(tamaño_bits//2))
    q = sympy.randprime(2**(tamaño_bits//2 - 1), 2**(tamaño_bits//2))
    # Calcular n y φ(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    # Elegir un exponente de cifrado e
    e = random.randint(2, phi_n - 1)
    while sympy.gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    # Calcular el exponente de descifrado d
    d = sympy.mod_inverse(e, phi_n)
    # Clave pública: (e, n), Clave privada: (d, n)
    clave_publica = (e, n)
    clave_privada = (d, n)
    return clave_publica, clave_privada
# Ejemplo de uso
tamaño_bits = 124  # Tamaño de las claves en bits
clave_publica, clave_privada = generar_claves(tamaño_bits)
print("Clave pública:", clave_publica)
print("Clave privada:", clave_privada)