n=int(input("enter a number"))
fact=1
if(n==1) or (n==0):
    print("the factorial is 1")
elif n>0:
    for i in range(1,n+1):
        fact=fact*i
    print("the factorial is", fact)
else:
    print("invalid output")
