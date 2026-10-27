def tail_sum(n, acc=0):
    if n ==0:
        return acc
    return tail_sum(n-1,acc+n)


input("tail recoursion - the last action is the recursiove call with accumulator. oress enter ")
print("tail_sum(4)=",tail_sum(4), "4+3+2+1")
print("tail_sum(5)=",tail_sum(5), "5+4+3+2+1")

n = int(input("enter a number (tr 3 or 6)"))

guess= input("what is a tail_sum("+ str(n)+")?")
print(guess)