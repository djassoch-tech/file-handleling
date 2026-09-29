n = int(input("enter a number"))

pos = 0

while n and not ( n  & 1):
    n >>= 1
    pos += 1

print(" first set bit position",pos)



