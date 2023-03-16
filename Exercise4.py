#this method of encription is called One Time Pad
#In Python, the xor between to int is given by the sign "^"
#a fuction for do xor between two bytes in python
def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

m1 = '158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf'
m2 = '73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2'
#remeber to switch from hex to bytes
print(xor(bytes.fromhex(m1),bytes.fromhex(m2)))