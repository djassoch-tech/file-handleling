n = int(input("enter your number :"))
print(bin(n)[2:])

if n > 0 and n & (n -1) ==0:
    print("power of 2")
else:
    print("not power of 2")