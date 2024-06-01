import random
import sympy
def generar_claves(tamaño_bits):
    #generar_numeros_primos_grandes_p_y_q
    p = sympy.randprime(2**(tamaño_bits//2 - 1), 2**(tamaño_bits//2))
    q = sympy.randprime(2**(tamaño_bits//2 - 1), 2**(tamaño_bits//2))
    #calcular_n_y_φ(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    #elegir_un_exponente_de_cifrado_e
    e = random.randint(2, phi_n - 1)
    while sympy.gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    #calcular_el_exponente_de_descifrado_d
    d = sympy.mod_inverse(e, phi_n)
    #clave_publica_(e_n)_Clave_privada_(d_n)
    clave_publica = (e, n)
    clave_privada = (d, n)
    return clave_publica, clave_privada
tamaño_bits = 124 #tamaño_de_las_claves_en_bits
clave_publica, clave_privada = generar_claves(tamaño_bits)
print("Clave pública:", clave_publica)
print("Clave privada:", clave_privada)