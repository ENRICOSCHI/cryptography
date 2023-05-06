m = 1076867677
n= 2147483647
c= 1265354953
s = 1862611659
i=0

v0 = (m*s+c)%n
print(0+v0)
for i in range(51):
    v0 = (m*v0+c)%n
    print(v0)

""""
v0 = (m*s+c)%n
v1 =(m*v0+c)%n
v2 =(m*v1+c)%n
v3 =(m*v2+c)%n
v4 =(m*v3+c)%n
v5 =(m*v4+c)%n
v6 =(m*v5+c)%n
v7 =(m*v6+c)%n
v8 =(m*v7+c)%n
v9=(m*v8+c)%n
v10 =(m*v9+c)%n

print("0" + str(v0))
print("1" + str(v1))
print("2" + str(v2))
print("3" + v3)
print("4" + v4)
print("5" + v5)
print("6" + v6)
print("7" + v7)
print("8" + v8)
print("9" + v9)
print("10" + v10)
"""