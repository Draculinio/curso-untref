def suma(n1,n2):
    return n1+n2

n = 0
while n < 10000000:
    n = suma(n, n+1)
    print(n)