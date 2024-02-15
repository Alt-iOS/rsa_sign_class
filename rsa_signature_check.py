from Crypto.Util import number as n
from Crypto.Hash import SHA256
import Crypto.Random as c

# Número de bits
bits = 1024

# Generación de primos para Alice (emisor)
pA = n.getPrime(bits, randfunc=c.get_random_bytes)
qA = n.getPrime(bits, randfunc=c.get_random_bytes)

# Calculamos n y phi(n) para Alice
nA = pA * qA
phiA = (pA - 1) * (qA - 1)

# Seleccionamos el exponente público e, comúnmente 65537
e = 65537

# Calculamos la clave privada d de Alice
dA = n.inverse(e, phiA)

# El mensaje
msg = "Hola Mundo"
print("Mensaje: ", msg)

# Hash del mensaje
hash_msg = SHA256.new(msg.encode("utf-8")).digest()

# Convertimos el hash a un número
m = int.from_bytes(hash_msg, byteorder="big")

# Firma del mensaje: se cifra el hash con la clave privada de Alice
signature = pow(m, dA, nA)
print("Firma: ", signature)

# Para verificar la firma, el receptor (o cualquier parte) usa la clave pública de Alice
# Se eleva la firma a la potencia de e modulo nA
hash_from_signature = pow(signature, e, nA)

# Convertimos el número obtenido de vuelta a bytes
hash_from_signature_bytes = int.to_bytes(
    hash_from_signature, len(hash_msg), byteorder="big"
)

# Comprobamos si el hash original y el obtenido de la firma coinciden
if hash_msg == hash_from_signature_bytes:
    print("La firma es válida.")
else:
    print("La firma no es válida.")
