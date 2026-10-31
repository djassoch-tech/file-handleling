input("head-tail - head is lst [0] base case is []. press enter")
print("[ 10, 20, 30] head:",[ 10, 20, 30][0],"tail:",[ 10, 20, 30][1:])
print(" [ 5, 15, 25] head:", [ 5, 15, 25][0],"tail:", [ 5, 15, 25][1:])

lst = [int(x) for x in input("enter 3 numbers separated by spaces:").split()]
guess = input("what is the head of " + str(lst) +"?")
input("head is lst[0] tail is lst[1]. press enter")
print("head ", lst[0], " your guess", guess)