n=4
print("=== Counting game Points (n=",n,"rounds)===")
print()

total =0
steps=0
print("formula way : total=",total," | steps =1" )
for round_num in range(1,n+1):
    total =+round_num
    steps +=1
    print("loop way : total=", total,"|steps =",steps)
    
    total =0
    steps=0
for round_num in range(1,n+1):
    for point in range(1,round_num+1):
        total += 1
        steps +=1
    print(" nested loop : total=", total,"|steps =",steps)

print()
print("=== now with n =",n,"rounds ===")
print()

