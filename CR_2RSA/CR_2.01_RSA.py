#level 1
print(2839360369 *3537287569)
#level 2
message = "This is the plaintext"
message_bytes = message.encode('utf-8')
m = int.from_bytes(message_bytes, byteorder='big')
print("m " + str(m))
#level 3
p = 3162364847
q = 3536576803
m = 1344495075812793855
e = 65537
n= p*q
c = pow(m, e, n)
print("c "+str(c))
#level 4
p = 2405177651
q = 4172988299
phi_n = (p - 1) * (q - 1)
#first print
print("tot(n) " + str(phi_n))
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - y * (a // b)
def modinv(a, m):
    d, x, y = extended_gcd(a, m)
    if d != 1:
        raise ValueError("No modular inverse exists")
    else:
        return x % m
e= 65537
d = modinv(e, phi_n)
#second print
print("d "+str(d))
#level 5
p = 2157135529
q = 4108064743
e = 65537
c = 7624505327763136566
n= p*q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print("m " + str(m))