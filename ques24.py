print("press 1 to add")
print("press 2 to subtract")
print("press 3 to multiply")
print("press 4 to divide")
choice=int(input("enter your choice "))
a=float(input("enter first number"))
b=float(input("enter second number"))
if choice==1:
    sum=a+b
    print("the answer is",sum)
elif choice==2:
    sub=a-b
    print("the answer is",sub)
elif choice==3:
    pro=a*b
    print("the answer is",pro)
elif choice==4:
    div=a/b
    print("the answer is",div)
elif choice==5:
    exit()
else:
    print("invalid input")







