v1=77243019
v0=1680462708
m=2115495185
n=2147483647
c = (v1 - m*v0) % n
v=v1
for i in range(51):
    v= (m*v+c)%n
    print(v)