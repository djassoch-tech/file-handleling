def sum_down(n):
    return 0 if n == 0 else n +sum_down(n-1)

n = int(input("enter number"))
print("sum =", sum_down(n),"| frammes:",n)