import itertools

ciphertext = bytes.fromhex('104e137f425954137f74107f525511457f5468134d7f146c4c')
print("A")
for key in itertools.product(range(32, 127), repeat=len(ciphertext)):
    print("B")
    key_bytes = bytes(key)
    print("C")
    plaintext = bytes([a ^ b for (a, b) in zip(ciphertext, key_bytes)])
    print("D")
    if b'flag{' in plaintext and plaintext[-1] == ord(b'}'):
        print("E")
        print("Plaintext:", plaintext)
