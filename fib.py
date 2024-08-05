n = int(input("enter the limit:"))
n1=0
n2=1
if n==1:
    print(n1)
elif n==2:
    print(n2)
else:
    print(n1)
    print(n2)
    while n>2:
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3)
        n-=1
