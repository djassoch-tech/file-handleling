n = int(input("enter number :"))
print("power of 4" if n > 0 and n & (n - 1) ==0 and n % 3 ==1 else "not a power of 4 ")