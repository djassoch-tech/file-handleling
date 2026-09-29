print("5 | 2 =",5 |2)
print("7 | 5 =",7 |5)


n = int(input("number:"))
if n > 0 and (n & (n-1))== 0:
    print("power of 2")
else:
    print("not power of 2")
