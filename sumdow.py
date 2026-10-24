def sum_down(n):
    if n ==0:
        return 0
    return n + sum_down(n-1)

input("recursion - a function calls itself until a base case stops it. press enter")
print("sum_down(3) = 3 + 2 + 1 + 0=",sum_down(3))
print("sum_down(4) = 4 + 3 + 2 + 1 + 0=",sum_down(4))

n = int(input("enter a number (try 5 or 6):"))
guess = input("what is sum_down(" + str(n)+")?")
input("sum_sown adds n to sum_down(n-1) until n recaches 0. press enter")
