# Práctica de algoritmo RSA
# Cifrado de mensaje

# 2024-02-14 - Anáhuac Mayab
import Crypto.Util.number as n
import Crypto as c

# Número de bits
bits = 1024

# Obtener los primos para Alice y Bob
pA = n.getPrime(bits, randfunc=c.Random.get_random_bytes)
print("pA: ", pA, "\n")
qA = n.getPrime(bits, randfunc=c.Random.get_random_bytes)
print("qA: ", qA, "\n")

pB = n.getPrime(bits, randfunc=c.Random.get_random_bytes)
print("pB: ", pB, "\n")
qB = n.getPrime(bits, randfunc=c.Random.get_random_bytes)
print("qB: ", qB, "\n")

# Obtenemos la primera parte de la lave publica de alice and bobo
nA = pA * qA
print("nA: ", nA, "\n")
nB = pB * qB
print("nB: ", nB, "\n")

# Calculamos la funcion phi de n
phiA = (pA - 1) * (qA - 1)
print("phiA: ", phiA, "\n")

phiB = (pB - 1) * (qB - 1)
print("phiB: ", phiB, "\n")

# Por razones de eficiencia utilizaremos el número 4 de Fermat, 65537, debido a que es
# un primo largo y no es potencia de 2, y como forma parte de la clave pública
# no  es necesario calcularlo
e = 65537

# Calculamos la clave privada de Alice y Bob
dA = n.inverse(e, phiA)
print("dA: ", dA, "\n")

dB = n.inverse(e, phiB)
print("dB: ", dB, "\n")

# El mensaje
msg = "Hola Mundo"
print("Mensaje: ", msg, "\n")
print("Longitud del mensaje: ", len(msg.encode("utf-8")), "\n")

# Convertimos el mensaje a un número
m = int.from_bytes(msg.encode("utf-8"), byteorder="big")
print("Mensaje convertido a número: ", m, "\n")

# Ciframos el mensaje
c = pow(m, e, nB)
print("Mensaje cifrado: ", c, "\n")

# Desciframos el mensaje
des = pow(c, dB, nB)
print("Mensaje descifrado: ", des, "\n")

msg_final = int.to_bytes(des, (des.bit_length() + 7) // 8, byteorder="big").decode(
    "utf-8"
)

print("Mensaje final: ", msg_final, "\n")
