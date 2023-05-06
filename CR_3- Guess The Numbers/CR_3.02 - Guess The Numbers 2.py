m = 2115495185
n = 2147483647
v0 = 1680462708
v1 = 77243019

for i in range(50):
    v2 = (m * v1 + v0) % n
    v0 = v1
    v1 = v2

print([v1] + [(m * v1 + v0) % n for i in range(49)])