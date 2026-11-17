def rotate(n):
    a = [1,2,3,4,5]
    n %=len(a)
    return a[n:] + a[:n]
input("press enter")
print(rotate(1), rotate(2))
n= int(input("rotate by:"))
print(rotate(n))