def m(n):
    return 0 if n ==0 else m(n-1)+2 * n

n = int(input())
print(m(n))