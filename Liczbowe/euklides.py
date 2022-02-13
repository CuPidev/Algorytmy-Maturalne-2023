def euklides(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a
def euklides2(a,b):
    if b > a:
        a, b = b, a
    while a!=b:
        a, b = b, a -b
    return a

print(euklides(8, 12))
print(euklides(8,12))
