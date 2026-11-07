def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    return ways(stairs - 1) + ways(stairs - 2)

input("ways counts every distinc path up n stairs - 1 step or 2 at a time. press enter")
print(" ways(3)=", ways(3))
print(" ways(4)=", ways(4))


n = int(input("enter number of stair( try 5 or 5): "))
guess = input("what is ways(" + str(n)+")?")
input("ways(stairs) = ways(stair - 1)+ ways(stair - 2) both branches always combine. press enter")
print("ways(" + str(n) +")=", ways(n),"your guess:", guess)
