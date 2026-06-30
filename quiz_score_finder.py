a= [12,24, 33,41,59,67,72,85,90,98];t=98

print("O(n):",a.index(t)+1,"steps")
l,h,s=0,len(a)-1,0
while l<=h:
    s+=1
    m=(l+h)//2
    l,h=((m+1,h)if a[m]<t else (l,m-1))if a[m]!=t else(h+1,h)
print("O(log n):",s,"steps")

def f(l,h,c=1):
    m = (l + h) // 2
    return c if a[m] ==t else f(m+1,h,c+1)
print("Rec:", f(0, len(a) - 1), "calls")
print("space:0(1), 0(log n)")
