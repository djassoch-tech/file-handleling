def count_paren(n, l=0, r=0):
    if l ==n and r ==n:
        return 1
    total = 0
    if l > r:
        total += count_paren(n, l,r+1)
    if l <n:
        total += count_paren(n, l+1,r)
    return total

input("count_paren counts every valid {} sequence - returms 1 at each valid end. press enter")
print(" count_parens(1)=",count_paren(1))
print(" count_parens(2)=",count_paren(2))

n = int(input("enter number of pairs( try 3 or 4):"))
guess = input("what is count_paren(" + str(n)+")")
print(guess)